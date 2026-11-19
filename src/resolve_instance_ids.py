"""
Make bare identifiers in a NARAD instance file absolute.

Instance data writes ids bare (RF_LASER, RF_LASER/FloorP, ...). LinkML's RDF dumper cannot expand a bare id
because the schema has no _base, so this step prefixes every identifier with a fixed root (file:///)
before `linkml-convert` runs. There is no per-facility namespace: load one facility per graph.

Why this step cannot be dropped in favour of `linkml-convert -P _base=file:///`: that works for plain ids,
but an id containing a colon (e.g. the BTA signal name btaMW006Cntl:horInDataM) is read as a CURIE whose
prefix is "btaMW006Cntl" and fails with "Unknown CURIE prefix". Prepending file:/// makes the whole string an
absolute IRI, so colons in ids are harmless.

The prefix is scaffolding only: src/llm/graph_init.cypher strips it again after the n10s import, so Neo4j
(and therefore the LLM) sees the bare ids. n10s needs a `uri` on every node, which is why the
prefix cannot simply be left off the RDF.

Example usage:
python3 src/resolve_instance_ids.py --instance_file examples/GUN_thru_MV.linkml.yaml \
        --output_file project/owl/GUN_thru_MV.linkml.resolved.yaml
"""
import argparse
import re

import yaml

# Slots whose values are identifiers (or references to them).
ID_KEYS = {"id", "subject", "object", "beamline_context"}
# Already absolute. Anything else (including signal names like btaMW006Cntl:horInDataM) is bare.
ABSOLUTE = re.compile(r"^(https?|tag|urn|file|ftp):", re.IGNORECASE)
# LinkML needs an absolute IRI for every id; this is the only "namespace".
NAMESPACE_ROOT = "file:///"


def resolve(node, namespace: str):
    if isinstance(node, dict):
        return {
            k: (namespace + v if k in ID_KEYS and isinstance(v, str) and not ABSOLUTE.match(v) else resolve(v, namespace))
            for k, v in node.items()
        }
    if isinstance(node, list):
        return [resolve(v, namespace) for v in node]
    return node


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--instance_file", required=True)
    ap.add_argument("--output_file", required=True)
    args = ap.parse_args()

    with open(args.instance_file, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    with open(args.output_file, "w", encoding="utf-8") as fh:
        yaml.safe_dump(resolve(data, NAMESPACE_ROOT), fh, sort_keys=False, allow_unicode=True)


if __name__ == "__main__":
    main()
