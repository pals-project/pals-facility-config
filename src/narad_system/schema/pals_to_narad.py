#!/usr/bin/env python3
"""Translate a PALS YAML lattice to a control-system-neutral NARAD skeleton.

Usage: python pals_to_narad.py -input INPUT_PALS_YAML -output OUTPUT_SKELETON_YAML
Run ``python pals_to_narad.py -help`` for option details.
"""

from __future__ import annotations

import argparse
import warnings
from collections import Counter
from copy import deepcopy
from pathlib import Path
import re
from typing import Any

import yaml


class PalsYamlLoader(yaml.SafeLoader):
    """Safe YAML loader that recognizes plain scientific-notation floats."""


PalsYamlLoader.add_implicit_resolver(
    "tag:yaml.org,2002:float",
    re.compile(r"^[+-]?[0-9][0-9_]*(?:\.[0-9_]*)?[eE][+-]?[0-9]+$"),
    list("-+0123456789"),
)

MAGNET_FUNCTIONS = {
    "Bend": ["Steering"],
    "Quadrupole": ["Focusing"],
    "Sextupole": ["Focusing"],
    "Kicker": ["Steering"],
}
DIRECT_PARAMETER_GROUPS = ("ReferenceP", "TwissP", "BodyShiftP")


def instance_id(name: str) -> str:
    """Return a stable local instance CURIE."""
    return f"inst:{name.upper()}"


def normalize_parameter_groups(entity: dict[str, Any], *, replace_ids: bool = False) -> None:
    """Add stable IDs and normalize aliases for inlined PALS parameter groups."""
    for group_name, group in entity.items():
        if not group_name.endswith("P") or not isinstance(group, dict):
            continue
        group_id = f"{entity['id']}/{group_name}"
        if replace_ids:
            group["id"] = group_id
        else:
            group.setdefault("id", group_id)
        if isinstance(group.get("alias"), str):
            group["alias"] = [group["alias"]]


def magnetic_multipoles(group: dict[str, Any]) -> dict[str, Any] | None:
    """Convert legacy Kn0/Ks1-style fields to the new mag_components list."""
    components: dict[int, dict[str, Any]] = {}
    for key, value in group.items():
        match = re.fullmatch(r"(Kn|Ks|Bn|Bs)(\d+)", key)
        if not match:
            continue
        field, order_text = match.groups()
        order = int(order_text)
        components.setdefault(order, {"order": order})[field] = value
    if not components:
        return None
    return {"mag_components": [components[n] for n in sorted(components)]}


def native_types(source: dict[str, Any]) -> list[str]:
    """Return source-system type identifiers for a PALS element."""
    values = [str(source["kind"])]
    bmad_key = source.get("Bmad", {}).get("Bmad_key")
    if bmad_key and bmad_key not in values:
        values.append(str(bmad_key))
    return values


def component_from_pals(name: str, source: dict[str, Any]) -> dict[str, Any] | None:
    """Map a supported PALS element to the current NARAD component schema."""
    source_kind = source.get("kind")
    target_kind = source_kind

    if source_kind in MAGNET_FUNCTIONS:
        functions = list(MAGNET_FUNCTIONS[source_kind])
    elif source_kind == "Instrument":
        target_kind = "DiagnosticDevice"
        functions = ["Measurement"]
    elif source_kind == "BeginningEle":
        functions = ["Mark"]
    elif source_kind == "Drift":
        functions = ["DriftSpace"]
    elif source_kind == "Marker":
        functions = ["Mark"]
    else:
        # Constants, controllers, and lattice/beamline container records are
        # not Component instances in the current NARAD schema.
        return None

    component: dict[str, Any] = {
        "id": instance_id(name),
        "kind": target_kind,
        "native_types": native_types(source),
        "functions": functions,
        "beamline_relation": "Inline",
    }

    if target_kind not in {"Marker", "BeginningEle"}:
        component["LongitudinalPlacementP"] = {
            "length": float(source.get("length", 0.0))
        }

    parameter_groups = (
        DIRECT_PARAMETER_GROUPS
        if target_kind != "Marker"
        else ("TwissP", "BodyShiftP")
    )
    for group_name in parameter_groups:
        if source.get(group_name):
            component[group_name] = deepcopy(source[group_name])

    if source.get("MetaP"):
        component["MetaP"] = deepcopy(source["MetaP"])
    if source.get("BendP"):
        component["BendP"] = deepcopy(source["BendP"])

    multipoles = magnetic_multipoles(source.get("MagneticMultipoleP", {}))
    if multipoles:
        component["MagneticMultipoleP"] = multipoles

    bmad_key = source.get("Bmad", {}).get("Bmad_key", "")
    if target_kind == "Kicker":
        if bmad_key == "HKicker":
            component["plane"] = "Horizontal"
        elif bmad_key == "VKicker":
            component["plane"] = "Vertical"

    normalize_parameter_groups(component)
    return component


def load_pals(
    path: Path,
) -> tuple[dict[str, Any], dict[str, dict[str, Any]], list[tuple[str, dict[str, Any]]]]:
    """Load named facility records and source beamlines."""
    with path.open(encoding="utf-8") as stream:
        document = yaml.load(stream, Loader=PalsYamlLoader)

    try:
        pals = document["PALS"]
        records = pals["facility"]
    except (KeyError, TypeError) as exc:
        raise ValueError("expected PALS.facility to be a list") from exc
    if not isinstance(records, list):
        raise ValueError("expected PALS.facility to be a list")

    named = {
        name: value
        for record in records
        if isinstance(record, dict)
        for name, value in record.items()
        if isinstance(value, dict)
    }
    beamlines = [(name, value) for name, value in named.items() if value.get("kind") == "BeamLine"]
    if not beamlines:
        raise ValueError("expected at least one BeamLine record")
    return pals, named, beamlines


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    """Recursively merge a PALS instance override onto a definition."""
    merged = deepcopy(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = deepcopy(value)
    return merged


def parse_line_item(item: Any) -> tuple[str, dict[str, Any]]:
    """Return the referenced name and optional inline PALS overrides."""
    if isinstance(item, str):
        return item, {}
    if isinstance(item, dict) and len(item) == 1:
        name, override = next(iter(item.items()))
        if override is None:
            return str(name), {}
        if isinstance(override, dict):
            return str(name), override
    raise ValueError(f"invalid BeamLine item: {item!r}")


def resolve_record(
    name: str,
    override: dict[str, Any],
    records: dict[str, dict[str, Any]],
    inheritance_stack: tuple[str, ...] = (),
) -> dict[str, Any]:
    """Resolve a named or inline record, including PALS inheritance."""
    if name in inheritance_stack:
        cycle = " -> ".join((*inheritance_stack, name))
        raise ValueError(f"cyclic PALS inheritance: {cycle}")

    record = deep_merge(records.get(name, {}), override)
    parent_name = record.pop("inherit", None)
    if parent_name is not None:
        parent = resolve_record(
            str(parent_name), {}, records, (*inheritance_stack, name)
        )
        record = deep_merge(parent, record)
    return record


def expand_beamline(
    name: str,
    override: dict[str, Any],
    records: dict[str, dict[str, Any]],
    expansion_stack: tuple[str, ...] = (),
) -> list[tuple[str, dict[str, Any]]]:
    """Recursively flatten nested BeamLines and signed repeat modifiers."""
    if name in expansion_stack:
        cycle = " -> ".join((*expansion_stack, name))
        raise ValueError(f"cyclic BeamLine reference: {cycle}")

    beamline = resolve_record(name, override, records)
    if beamline.get("kind") != "BeamLine":
        raise ValueError(f"{name!r} is referenced as a BeamLine but has no kind: BeamLine")

    expanded: list[tuple[str, dict[str, Any]]] = []
    for item in beamline.get("line", []):
        item_name, item_override = parse_line_item(item)
        resolved = resolve_record(item_name, item_override, records)
        repeat = int(resolved.pop("repeat", 1))
        if repeat == 0:
            continue

        if resolved.get("kind") == "BeamLine":
            occurrences = expand_beamline(
                item_name,
                item_override,
                records,
                (*expansion_stack, name),
            )
        else:
            occurrences = [(item_name, resolved)]

        if repeat < 0:
            occurrences = list(reversed(occurrences))
        for _ in range(abs(repeat)):
            expanded.extend(deepcopy(occurrences))
    return expanded


def build_document(source_path: Path) -> dict[str, Any]:
    """Build a signal-free NARAD skeleton from a PALS export."""
    pals, records, source_beamlines = load_pals(source_path)
    named_components = {
        name: component
        for name, source in records.items()
        if (component := component_from_pals(name, source)) is not None
    }

    components: list[dict[str, Any]] = []
    component_ids: set[str] = set()
    used_names: set[str] = set()
    relations: list[dict[str, Any]] = []
    beamlines: list[dict[str, Any]] = []

    for beamline_name, beamline in source_beamlines:
        expanded_line = expand_beamline(beamline_name, {}, records)
        supported_line = [
            (name, component)
            for name, source in expanded_line
            if (component := component_from_pals(name, source)) is not None
        ]
        occurrence_totals = Counter(name for name, _ in supported_line)
        occurrence_numbers: Counter[str] = Counter()
        ordered_ids: list[str] = []
        for name, source_component in supported_line:
            component = deepcopy(source_component)
            if occurrence_totals[name] > 1:
                occurrence_numbers[name] += 1
                suffix = f"{occurrence_numbers[name]:03d}"
                if len(source_beamlines) > 1:
                    suffix = f"{beamline_name}_{suffix}"
                component["id"] = instance_id(f"{name}_{suffix}")
                normalize_parameter_groups(component, replace_ids=True)
            if component["id"] not in component_ids:
                components.append(component)
                component_ids.add(component["id"])
            ordered_ids.append(component["id"])
            used_names.add(name)

        beamline_id = instance_id(beamline_name)
        relations.extend(
            {
                "id": f"inst:{beamline_name.upper()}_{subject[5:]}_PRECEDES_{obj[5:]}",
                "subject": subject,
                "predicate": "pals:precedes",
                "object": obj,
                "context": "beamline_order",
                "beamline_context": beamline_id,
            }
            for subject, obj in zip(ordered_ids, ordered_ids[1:])
        )
        beamlines.append(
            {
                "id": beamline_id,
                "kind": "BeamLine",
                "functions": ["BeamLineSection"],
                "beamline_relation": "Inline",
                "multipass": False,
                "periodic": bool(beamline.get("periodic", False)),
                "description": f"Beamline imported from PALS record {beamline_name}.",
            }
        )

    components.extend(
        component for name, component in named_components.items() if name not in used_names
    )

    source_notes = pals.get("notes", [])
    notes = list(source_notes) if isinstance(source_notes, list) else [str(source_notes)]
    notes.append("Generated from PALS source data without control-system enrichment.")

    return {
        "description": f"Control-system-neutral NARAD skeleton generated from {source_path.name}.",
        "kind": "PALSAccelerator",
        "version": "0.1.0",
        "notes": notes,
        "facility": {
            "components": components,
            "beamlines": beamlines,
            "signals": [],
            "signal_bindings": [],
            "component_relations": relations,
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("-help", action="help", help="show this help message and exit")
    parser.add_argument(
        "-input",
        "--input",
        type=Path,
        required=True,
        metavar="INPUT_PALS_YAML",
        help="PALS YAML file to translate, expected format: 'filename.pals.yaml'",
    )
    parser.add_argument(
        "-output",
        "--output",
        type=Path,
        required=False,
        default=None,
        metavar="OUTPUT_SKELETON_YAML",
        help="NARAD skeleton YAML file to create. Defaults to 'filename_narad_skeleton.yaml' if input follows 'filename.pals.yaml' format.",
    )

    args = parser.parse_args()

    # Try to derive default output name from input name
    if args.output is None:
        input_name = args.input.name  # e.g. "fodo.pals.yaml"
        parts = input_name.split(".")

        # Expect format: "filename.pals.yaml" → exactly 3 parts with middle part "pals"
        if len(parts) == 3 and parts[1] == "pals" and parts[2] == "yaml":
            args.output = args.input.parent / f"{parts[0]}_narad_skeleton.yaml"
        else:
            warnings.warn(
                f"Input file '{input_name}' does not follow expected 'filename.pals.yaml' format. "
                f"Cannot derive default output name. Please provide an output file with -output.",
                UserWarning,
                stacklevel=2,
            )
            parser.error(
                f"Could not derive output file name from '{input_name}'. "
                f"Please provide -output explicitly."
            )

    return args


def main() -> None:
    args = parse_args()
    document = build_document(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as stream:
        yaml.safe_dump(document, stream, sort_keys=False, allow_unicode=True, width=100)
    facility = document["facility"]
    print(
        f"Wrote {args.output} with {len(facility['components'])} components, "
        f"{len(facility['component_relations'])} beamline-order relations, "
        "and no control-system signals."
    )


if __name__ == "__main__":
    main()
