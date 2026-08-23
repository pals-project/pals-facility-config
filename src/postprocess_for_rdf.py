from rdflib import Graph, URIRef, RDF, Literal, Namespace
import argparse

PALS = Namespace("https://pals-project.readthedocs.io/")

# class_uri overrides for predicate-designating (relation) classes —
# everything else defaults to PALS[<bare class name>]
PREDICATE_URI = {
    "HasSignal": PALS.has_signal,
    "HasSetpointSignal": PALS.has_setpoint_signal,
    "HasReadbackSignal": PALS.has_readback_signal,
    "HasCommandSignal": PALS.has_command_signal,
    "HasLimitSignal": PALS.has_limit_signal,
    "Precedes": PALS.precedes,
    "Contains": PALS.contains,
    "Controls": PALS.controls,
    "IsPartOf": PALS.is_part_of,
    "AdjacentTo": PALS.adjacent_to,
    "Overlaps": PALS.overlaps,
    "HasConnectingBranch": PALS.has_connecting_branch,
    "MountedOn": PALS.mounted_on,
    "Intersects": PALS.intersects,
    "NearestTo": PALS.nearest_to,
}

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
            "--instance_file", default="project/owl/core_acc_narad_instance.ttl",
            help="Path to the instance file (RDF graph) to postprocess",
        )
    ap.add_argument(
        "--output_file", default="project/owl/core_acc_narad_instance_rdf.ttl",
        help="Path to the output postprocessed RDF graph (default: project/owl/core_acc_narad_instance_rdf.ttl)",
    )
    args = ap.parse_args()

    g = Graph()
    g.parse(args.instance_file, format="turtle")

    RDF_PREDICATE = URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#predicate")

    for s, p, o in list(g.triples((None, RDF.type, None))):
        if isinstance(o, Literal):
            g.remove((s, p, o))
            g.add((s, p, PALS[str(o)]))   # bare class name -> pals:ClassName

    for s, p, o in list(g.triples((None, RDF_PREDICATE, None))):
        if isinstance(o, Literal):
            g.remove((s, p, o))
            g.add((s, p, PREDICATE_URI[str(o)]))

    # Materialize each reified relationship as a direct RDF triple.
    for relation, _, predicate in list(g.triples((None, RDF.predicate, None))):
        subject = g.value(relation, RDF.subject)
        obj = g.value(relation, RDF.object)

        if (
            subject is not None
            and obj is not None
            and isinstance(predicate, URIRef)
        ):
            g.add((subject, predicate, obj))

    CLASS_FOR_PREDICATE = {uri: PALS[name] for name, uri in PREDICATE_URI.items()}

    # Reverse lookup: predicate URI -> relation class
    for relation, _, predicate in list(g.triples((None, RDF.predicate, None))):
        subject = g.value(relation, RDF.subject)
        obj = g.value(relation, RDF.object)

        # Directly assert the reified relation's type, e.g. inst:IFYK203_to_ISLK302 a pals:Precedes
        if predicate in CLASS_FOR_PREDICATE:
            g.add((relation, RDF.type, CLASS_FOR_PREDICATE[predicate]))

        if (
            subject is not None
            and obj is not None
            and isinstance(predicate, URIRef)
        ):
            g.add((subject, predicate, obj))

    g.serialize(destination=args.output_file, format="turtle")

if __name__ == "__main__":
    main()