from pathlib import Path
from rdflib import Graph
import argparse

def main():
    """
    Merges a data instance graph with a schema graph and generates template files for the merged schema.


    python3 merge_graphs.py \
        --schema_file <input_schema_file_full_path> \
        --instance_file <instance_file_full_path> \
        --output_file <output_file_full_path> \

    Example usage:
    python3 merge_graphs.py \
        --schema_file project/owl/narad.owl.ttl \
        --instance_file project/owl/core_acc_narad_instance.ttl \ 
        --output_file project/owl/narad_full.ttl
    """
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--schema_file", help="Path to LinkML schema YAML")
    ap.add_argument(
            "--instance_file", default=None,
            help="Path to the instance file (RDF graph) to merge with the schema",
        )
    ap.add_argument(
        "--output_file", default="project/owl/narad_full.ttl",
        help="Path to the output merged RDF graph (default: project/owl/narad_full.ttl)",
    )
    args = ap.parse_args()
    
    outfile = Path(args.output_file)
    outfile.parent.mkdir(parents=True, exist_ok=True)

    combined = Graph()
    combined.parse(args.schema_file, format="turtle")
    combined.parse(args.instance_file, format="turtle")
    combined.serialize(destination=str(outfile), format="turtle")

if __name__ == "__main__":
    main()