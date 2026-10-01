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

def main():
    """
    Postprocesses the RDF graph to replace bare class names with PALS URIs for predicate-designating classes.

    This script reads an RDF graph from 'project/owl/core_acc_narad_instance.ttl', replaces bare class names
    with their corresponding PALS URIs for predicate-designating classes, and writes the modified graph back
    to the same file.

    Example usage:
    python3 postprocess_for_rdf.py \
            --instance_file <instance_file_full_path> \
            --output_file <output_file_full_path> \
            
    Example usage:
    python3 postprocess_for_rdf.py --instance_file project/owl/core_acc_narad_instance.ttl --output_file project/owl/core_acc_narad_instance_rdf.ttl

    """
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument(
                "--schema", default="src/narad/schema/narad.yaml",
                help="Path to the LinkML schema file",
            )
    ap.add_argument(
            "--instance_file", default="project/owl/core_acc_narad_instance.ttl",
            help="Path to the instance file (RDF graph) to postprocess",
        )
    ap.add_argument(
        "--output_file", default="project/owl/core_acc_narad_instance_rdf.ttl",
        help="Path to the output postprocessed RDF graph (default: project/owl/core_acc_narad_instance_rdf.ttl)",
    )
    args = ap.parse_args()

    predicate_uri = load_predicate_uris(args.schema)
    class_for_predicate = {uri: PALS[name] for name, uri in predicate_uri.items()}

    g = Graph()
    g.parse(args.instance_file, format="turtle")


    for s, p, o in list(g.triples((None, RDF.type, None))):
        if isinstance(o, Literal):
            g.remove((s, p, o))
            g.add((s, p, PALS[str(o)]))   # bare class name -> pals:ClassName

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

    g.serialize(destination=args.output_file, format="turtle")

if __name__ == "__main__":
    main()