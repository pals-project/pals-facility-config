"""
Make bare identifiers in a NARAD instance file absolute, using the file's own Facility.id_namespace.

Instance data writes ids bare (RF_LASER, RF_LASER/FloorP, ...). LinkML's RDF dumper cannot expand a bare id
because the schema deliberately has no schema-wide _base (each facility declares its own id_namespace instead),
so this step prefixes every identifier with id_namespace before `linkml-convert` runs.

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
    namespace = (data.get("facility") or {}).get("id_namespace")
    if not namespace:
        raise SystemExit(f"{args.instance_file}: facility.id_namespace is required to resolve identifiers")

    with open(args.output_file, "w", encoding="utf-8") as fh:
        yaml.safe_dump(resolve(data, namespace), fh, sort_keys=False, allow_unicode=True)


if __name__ == "__main__":
    main()
