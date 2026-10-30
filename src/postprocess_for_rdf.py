import re
from rdflib import Graph, URIRef, RDF, Literal, Namespace
import argparse
from linkml_runtime.utils.schemaview import SchemaView

PALS = Namespace("https://pals-project.readthedocs.io/")


# RELATION_MAP is NOT USED in this script, but is provided for reference. It maps bare class names to their corresponding PALS relation classes and predicates.
RELATION_MAP = {
    "HasSignal": {
        "class": PALS.HasSignalRelation,
        "predicate": PALS.has_signal,
    },
    "HasSetpointSignal": {
        "class": PALS.HasSetpointSignalRelation,
        "predicate": PALS.has_setpoint_signal,
    },
    "HasReadbackSignal": {
        "class": PALS.HasReadbackSignalRelation,
        "predicate": PALS.has_readback_signal,
    },
    "HasCommandSignal": {
        "class": PALS.HasCommandSignalRelation,
        "predicate": PALS.has_command_signal,
    },
    "HasLimitSignal": {
        "class": PALS.HasLimitSignalRelation,
        "predicate": PALS.has_limit_signal,
    },
    "Precedes": {
        "class": PALS.PrecedesRelation,
        "predicate": PALS.precedes,
    },
    "Contains": {
        "class": PALS.ContainsRelation,
        "predicate": PALS.contains,
    },
    "Controls": {
        "class": PALS.ControlsRelation,
        "predicate": PALS.controls,
    },
    "IsPartOf": {
        "class": PALS.IsPartOfRelation,
        "predicate": PALS.is_part_of,
    },
    "AdjacentTo": {
        "class": PALS.AdjacentToRelation,
        "predicate": PALS.adjacent_to,
    },
    "Overlaps": {
        "class": PALS.OverlapsRelation,
        "predicate": PALS.overlaps,
    },
    "HasConnectingBranch": {
        "class": PALS.HasConnectingBranchRelation,
        "predicate": PALS.has_connecting_branch,
    },
    "MountedOn": {
        "class": PALS.MountedOnRelation,
        "predicate": PALS.mounted_on,
    },
    "Intersects": {
        "class": PALS.IntersectsRelation,
        "predicate": PALS.intersects,
    },
    "NearestTo": {
        "class": PALS.NearestToRelation,
        "predicate": PALS.nearest_to,
    },
}

def load_predicate_uris(schema_path: str) -> dict[str, URIRef]:
    """Map each concrete Edge subclass name to the expanded URI in its rdf_predicate annotation."""
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
        mapping[class_name] = URIRef(schema_view.expand_curie(str(annotation.value)))

    if missing:
        raise ValueError(
            "Concrete Edge classes missing an 'rdf_predicate' annotation: "
            + ", ".join(sorted(missing))
        )
    return mapping

_BASE_LINE = re.compile(r"^@base\s+<([^<>]*)>\s*\.\s*$", re.MULTILINE)
_RELATIVE_IRI = re.compile(r"<([^<>:\s]*)>")  # an IRI reference with no scheme/colon


def absolutize_turtle(text: str) -> str:
    """
    Drop the @base line and rewrite relative IRIs (e.g. <ICBK403>) as absolute IRIs by plain concatenation.

    Facility.id_namespace is a tag:/urn: style base, which has no '//' and which RFC 3986 resolvers (rdflib's
    parser, RDF4J/n10s) handle inconsistently. The namespace is required to end in '/', '#' or ':', so
    concatenation is what it means.
    """
    match = _BASE_LINE.search(text)
    if match is None:
        return text
    base = match.group(1)
    text = _BASE_LINE.sub("", text, count=1)
    return _RELATIVE_IRI.sub(lambda m: f"<{base}{m.group(1)}>", text)


def main():
    """
    Postprocesses the RDF graph to replace bare class names with PALS URIs for predicate-designating classes.

    This script reads an RDF graph from 'project/owl/GUN_thru_MV.linkml.ttl', replaces bare class names
    with their corresponding PALS URIs for predicate-designating classes, and writes the modified graph back
    to the same file.

    Example usage:
    python3 postprocess_for_rdf.py \
            --instance_file <instance_file_full_path> \
            --output_file <output_file_full_path> \
            
    Example usage:
    python3 postprocess_for_rdf.py --instance_file project/owl/GUN_thru_MV.linkml.ttl --output_file project/owl/GUN_thru_MV.linkml_rdf.ttl

    """
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument(
                "--schema", default="src/narad/schema/narad.yaml",
                help="Path to the LinkML schema file",
            )
    ap.add_argument(
            "--instance_file", default="project/owl/GUN_thru_MV.linkml.ttl",
            help="Path to the instance file (RDF graph) to postprocess",
        )
    ap.add_argument(
        "--output_file", default="project/owl/GUN_thru_MV.linkml_rdf.ttl",
        help="Path to the output postprocessed RDF graph (default: project/owl/GUN_thru_MV.linkml_rdf.ttl)",
    )
    args = ap.parse_args()

    predicate_uri = load_predicate_uris(args.schema)
    schema_view = SchemaView(args.schema)
    all_classes = schema_view.all_classes()

    def class_uri(name: str) -> URIRef:
        """Expanded URI of a schema class, e.g. BeamProfileMonitor -> acc:BeamProfileMonitor (the schema's default_prefix)."""
        return URIRef(schema_view.get_uri(name, expand=True))

    class_for_predicate = {uri: class_uri(name) for name, uri in predicate_uri.items()}

    g = Graph()
    with open(args.instance_file, encoding="utf-8") as fh:
        g.parse(data=absolutize_turtle(fh.read()), format="turtle")


    unknown_kinds = sorted({
        str(o) for _, _, o in g.triples((None, RDF.type, None))
        if isinstance(o, Literal) and str(o) not in all_classes
    })
    if unknown_kinds:
        raise ValueError(f"Instance uses kinds that are not classes in the schema: {', '.join(unknown_kinds)}")

    for s, p, o in list(g.triples((None, RDF.type, None))):
        if isinstance(o, Literal):
            g.remove((s, p, o))
            g.add((s, p, class_uri(str(o))))   # bare class name -> same URI the generated OWL gives the class

    unknown = sorted({
        str(o) for _, _, o in g.triples((None, RDF.predicate, None))
        if isinstance(o, Literal) and str(o) not in predicate_uri
    })
    if unknown:
        raise ValueError(f"Instance uses predicates with no rdf_predicate mapping in the schema: {', '.join(unknown)}")

    for s, p, o in list(g.triples((None, RDF.predicate, None))):
        if isinstance(o, Literal):
            g.remove((s, p, o))
            g.add((s, p, predicate_uri[str(o)]))


    for relation, _, predicate in list(g.triples((None, RDF.predicate, None))):
        subject = g.value(relation, RDF.subject)
        obj = g.value(relation, RDF.object)
        if predicate in class_for_predicate:
            g.add((relation, RDF.type, class_for_predicate[predicate]))
        if subject is not None and obj is not None and isinstance(predicate, URIRef):
            g.add((subject, predicate, obj))

    # absolutize_turtle() made every node IRI absolute, and no base= is passed here, so the output has no @base line.
    g.serialize(destination=args.output_file, format="turtle")

if __name__ == "__main__":
    main()