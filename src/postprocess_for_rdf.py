import argparse
import re

from linkml_runtime.utils.schemaview import SchemaView
from rdflib import Graph, Literal, RDF, URIRef


def load_predicate_uris(schema_path: str) -> dict[str, URIRef]:
    """Map each concrete Edge subclass to its annotated RDF predicate URI."""
    schema_view = SchemaView(schema_path)
    mapping: dict[str, URIRef] = {}
    missing: list[str] = []

    for class_name in schema_view.class_descendants("Edge", reflexive=False):
        class_def = schema_view.get_class(class_name)
        if class_def.abstract:
            continue
        annotation = class_def.annotations.get("rdf_predicate")
        if annotation is None:
            missing.append(class_name)
            continue
        mapping[class_name] = URIRef(
            schema_view.expand_curie(str(annotation.value))
        )

    if missing:
        raise ValueError(
            "Concrete Edge classes missing an 'rdf_predicate' annotation: "
            + ", ".join(sorted(missing))
        )
    return mapping


_BASE_LINE = re.compile(r"^@base\s+<([^<>]*)>\s*\.\s*$", re.MULTILINE)
_RELATIVE_IRI = re.compile(r"<([^<>:\s]*)>")


def absolutize_turtle(text: str) -> str:
    """Remove Turtle's base declaration and make relative IRIs absolute."""
    match = _BASE_LINE.search(text)
    if match is None:
        return text
    base = match.group(1)
    text = _BASE_LINE.sub("", text, count=1)
    return _RELATIVE_IRI.sub(lambda item: f"<{base}{item.group(1)}>", text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--schema", default="src/narad/schema/narad.yaml")
    parser.add_argument("--instance_file", required=True)
    parser.add_argument("--output_file", required=True)
    args = parser.parse_args()

    predicate_uris = load_predicate_uris(args.schema)
    schema_view = SchemaView(args.schema)
    all_classes = schema_view.all_classes()

    def class_uri(name: str) -> URIRef:
        return URIRef(schema_view.get_uri(name, expand=True))

    classes_for_predicates = {
        uri: class_uri(name) for name, uri in predicate_uris.items()
    }

    graph = Graph()
    with open(args.instance_file, encoding="utf-8") as input_file:
        graph.parse(data=absolutize_turtle(input_file.read()), format="turtle")

    unknown_kinds = sorted(
        {
            str(value)
            for _, _, value in graph.triples((None, RDF.type, None))
            if isinstance(value, Literal) and str(value) not in all_classes
        }
    )
    if unknown_kinds:
        raise ValueError(
            "Instance uses kinds that are not classes in the schema: "
            + ", ".join(unknown_kinds)
        )

    for subject, predicate, value in list(
        graph.triples((None, RDF.type, None))
    ):
        if isinstance(value, Literal):
            graph.remove((subject, predicate, value))
            graph.add((subject, predicate, class_uri(str(value))))

    unknown_predicates = sorted(
        {
            str(value)
            for _, _, value in graph.triples((None, RDF.predicate, None))
            if isinstance(value, Literal) and str(value) not in predicate_uris
        }
    )
    if unknown_predicates:
        raise ValueError(
            "Instance uses predicates with no rdf_predicate mapping: "
            + ", ".join(unknown_predicates)
        )

    for relation, predicate_slot, value in list(
        graph.triples((None, RDF.predicate, None))
    ):
        if isinstance(value, Literal):
            graph.remove((relation, predicate_slot, value))
            graph.add((relation, predicate_slot, predicate_uris[str(value)]))

    for relation, _, predicate in list(
        graph.triples((None, RDF.predicate, None))
    ):
        subject = graph.value(relation, RDF.subject)
        object_ = graph.value(relation, RDF.object)
        if predicate in classes_for_predicates:
            graph.add((relation, RDF.type, classes_for_predicates[predicate]))
        if subject is not None and object_ is not None and isinstance(predicate, URIRef):
            graph.add((subject, predicate, object_))

    graph.serialize(destination=args.output_file, format="turtle")


if __name__ == "__main__":
    main()
