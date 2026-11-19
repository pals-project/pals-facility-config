import argparse
from pathlib import Path

from rdflib import Graph


def main():
    """Merge a data instance graph with a schema graph."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--schema_file", required=True)
    parser.add_argument("--instance_file", required=True)
    parser.add_argument("--output_file", default="project/owl/narad_full.ttl")
    args = parser.parse_args()

    output = Path(args.output_file)
    output.parent.mkdir(parents=True, exist_ok=True)

    combined = Graph()
    combined.parse(args.schema_file, format="turtle")
    combined.parse(args.instance_file, format="turtle")
    combined.serialize(destination=str(output), format="turtle")


if __name__ == "__main__":
    main()
