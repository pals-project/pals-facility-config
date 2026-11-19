"""Make bare identifiers in a NARAD instance absolute before RDF conversion."""

import argparse
import re

import yaml


ID_KEYS = {"id", "subject", "object", "beamline_context"}
ABSOLUTE = re.compile(r"^(https?|tag|urn|file|ftp):", re.IGNORECASE)
NAMESPACE_ROOT = "file:///"


def resolve(node, namespace: str):
    if isinstance(node, dict):
        return {
            key: (
                namespace + value
                if key in ID_KEYS
                and isinstance(value, str)
                and not ABSOLUTE.match(value)
                else resolve(value, namespace)
            )
            for key, value in node.items()
        }
    if isinstance(node, list):
        return [resolve(value, namespace) for value in node]
    return node


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--instance_file", required=True)
    parser.add_argument("--output_file", required=True)
    args = parser.parse_args()

    with open(args.instance_file, encoding="utf-8") as stream:
        data = yaml.safe_load(stream)
    with open(args.output_file, "w", encoding="utf-8") as stream:
        yaml.safe_dump(
            resolve(data, NAMESPACE_ROOT),
            stream,
            sort_keys=False,
            allow_unicode=True,
        )


if __name__ == "__main__":
    main()
