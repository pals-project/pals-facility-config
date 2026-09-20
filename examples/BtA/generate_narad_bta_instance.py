#!/usr/bin/env python3
"""Enrich a control-neutral NARAD skeleton with BtA device and ADO data.

Usage: python generate_narad_bta_instance.py -input INPUT_SKELETON_YAML -output OUTPUT_NARAD_YAML
Run ``python generate_narad_bta_instance.py -help`` for option details.
"""

from __future__ import annotations

import argparse
from copy import deepcopy
from pathlib import Path
import re
from typing import Any

import yaml

from narad.datamodel import narad_pydantic as narad_model


DEFAULT_INPUT = Path(__file__).with_name("bta_narad_skeleton_palsparserpy.yaml")
DEFAULT_OUTPUT = Path(__file__).with_name("bta_narad_instance.yaml")

MW_DEVICE_INFO = {
    "native_type": "Multiwire",
    "description": "Multiwire beam-profile monitor.",
    "devices": {
        "MW006": {"nbr_wires_x": 32, "nbr_wires_y": 32, "spacing_x": 0.0015, "spacing_y": 0.0015},
        "MW060": {"nbr_wires_x": 32, "nbr_wires_y": 32, "spacing_x": 0.0025, "spacing_y": 0.0025},
        "MW125": {"nbr_wires_x": 32, "nbr_wires_y": 32, "spacing_x": 0.0025, "spacing_y": 0.0025},
        "MW166": {"nbr_wires_x": 32, "nbr_wires_y": 32, "spacing_x": 0.0025, "spacing_y": 0.0025},
        "MWA15": {"nbr_wires_x": 64, "nbr_wires_y": 32, "spacing_x": 0.002, "spacing_y": 0.002},
    },
}

BTA_KIND_RULES = (
    {
        "name_pattern": r"^PUE",
        "source_kind": "DiagnosticDevice",
        "target_kind": "BeamPositionMonitor",
    },
    {
        "names": frozenset(MW_DEVICE_INFO["devices"]),
        "source_kind": "DiagnosticDevice",
        "target_kind": "BeamProfileMonitor",
    },
)

ADO_RULES = {
    "Quadrupole": {
        "current_setpoint": [(r"QH0*([1-9][0-9]*)", (r"bta-qf\1-ps", "setpointS")), (r"QV0*([1-9][0-9]*)", (r"bta-qd\1-ps", "setpointS"))],
        "current_readback": [(r"QH0*([1-9][0-9]*)", (r"bta-qf\1-ps", "currentM")), (r"QV0*([1-9][0-9]*)", (r"bta-qd\1-ps", "currentM"))],
        "current_range": [(r"QH0*([1-9][0-9]*)", (r"bta-qf\1-ps", "rangeC")), (r"QV0*([1-9][0-9]*)", (r"bta-qd\1-ps", "rangeC"))],
        "magnet_status": [(r"QH0*([1-9][0-9]*)", (r"bta-qf\1-ps", "stateS")), (r"QV0*([1-9][0-9]*)", (r"bta-qd\1-ps", "stateS"))],
    },
    "Kicker": {
        "current_setpoint": [(r"DV0*([1-9][0-9]*)", (r"bta-tv\1-ps", "setpointS")), (r"DH0*([1-9][0-9]*)", (r"bta-th\1-ps", "setpointS"))],
        "current_readback": [(r"DV0*([1-9][0-9]*)", (r"bta-tv\1-ps", "currentM")), (r"DH0*([1-9][0-9]*)", (r"bta-th\1-ps", "currentM"))],
        "current_range": [(r"DV0*([1-9][0-9]*)", (r"bta-tv\1-ps", "rangeC")), (r"DH0*([1-9][0-9]*)", (r"bta-th\1-ps", "rangeC"))],
        "magnet_status": [(r"DV0*([1-9][0-9]*)", (r"bta-tv\1-ps", "stateS")), (r"DH0*([1-9][0-9]*)", (r"bta-th\1-ps", "stateS"))],
    },
    "BeamProfileMonitor": {
        "horizontal_profile": [(r"MWA([0-9]+)", (r"adrA\1MWCntl", "horInDataM")), (r"MW([0-9]+)", (r"btaMW\1Cntl", "horInDataM"))],
        "vertical_profile": [(r"MWA([0-9]+)", (r"adrA\1MWCntl", "verInDataM")), (r"MW([0-9]+)", (r"btaMW\1Cntl", "verInDataM"))],
        "insertion_status": [(r"MWA([0-9]+)", (r"adrA\1MWCntl", "harpIsM")), (r"MW([0-9]+)", (r"btaMW\1Cntl", "harpIsM"))],
    },
}

ADO_SIGNAL_SPECS = {
    "current_setpoint": {
        "signal_role": "Setpoint", "native_description": "Desired magnet current command.",
        "canonical_signal_type": "MagnetCurrentSetpoint", "quantity_kind": "ElectricCurrent",
        "native_data_type": "Float", "native_unit": "A", "predicate": "pals:has_setpoint_signal",
    },
    "current_readback": {
        "signal_role": "Readback", "native_description": "Measured magnet current.",
        "canonical_signal_type": "MagnetCurrentReadback", "quantity_kind": "ElectricCurrent",
        "native_data_type": "Float", "native_unit": "A", "predicate": "pals:has_readback_signal",
    },
    "current_range": {
        "signal_role": "RangeLimit", "native_description": "Allowed magnet-current range returned as [maximum, minimum].",
        "canonical_signal_type": "MagnetCurrentRange", "quantity_kind": "ElectricCurrent",
        "native_data_type": "FloatArray", "native_unit": "A", "predicate": "pals:has_limit_signal",
        "MetaP": {"additional_metadata": [
            {"key": "array_order", "value": "maximum,minimum", "datatype": "String"},
            {"key": "array_length", "value": "2", "datatype": "Integer"},
        ]},
    },
    "magnet_status": {
        "signal_role": "Status", "native_description": "Power-supply or device state summary.",
        "canonical_signal_type": "Status", "quantity_kind": "State",
        "native_data_type": "String", "native_unit": "none", "predicate": "pals:has_signal",
    },
    "horizontal_profile": {
        "signal_role": "Readback", "native_description": "Measured horizontal multiwire beam-intensity profile.",
        "canonical_signal_type": "HorizontalBeamPosition", "quantity_kind": "BeamPosition",
        "native_data_type": "FloatArray", "native_unit": "V", "predicate": "pals:has_readback_signal",
    },
    "vertical_profile": {
        "signal_role": "Readback", "native_description": "Measured vertical multiwire beam-intensity profile.",
        "canonical_signal_type": "VerticalBeamPosition", "quantity_kind": "BeamPosition",
        "native_data_type": "FloatArray", "native_unit": "V", "predicate": "pals:has_readback_signal",
    },
    "insertion_status": {
        "signal_role": "Status", "native_description": "Insertion status of the multiwire monitor.",
        "canonical_signal_type": "Status", "quantity_kind": "State",
        "native_data_type": "String", "native_unit": "none", "predicate": "pals:has_signal",
    },
}

ADO_SIGNAL_DEFAULTS = {
    "kind": "Signal",
    "source_system": "Other",
    "access_protocol": "ADO",
}

BTA_DOCUMENT_ENRICHMENT = {
    "facility_identifiers": [
        {"identifier_type": "LOCAL", "identifier_value": "BTA"},
    ],
    "description": "NARAD representation of the BtA beamline enriched with ADO controls.",
    "notes": [
        "Enriched with BtA device properties and ADO signal naming rules.",
    ],
}


def local_name(identifier: str) -> str:
    return identifier.removeprefix("inst:")


def default_functions(kind: str) -> list[str]:
    """Read a component kind's nearest schema-defined default function."""
    model = getattr(narad_model, kind)
    for ancestor in model.__mro__:
        metadata = ancestor.__dict__.get("linkml_meta")
        if metadata is None:
            continue
        annotation = dict(metadata).get("annotations", {}).get("default_function")
        if annotation is not None:
            value = annotation.get("value") if isinstance(annotation, dict) else annotation
            return [str(value)]
    raise ValueError(f"NARAD component kind {kind} has no default_function annotation")


def metadata_datatype(value: Any) -> str:
    if isinstance(value, bool):
        return "Boolean"
    if isinstance(value, int):
        return "Integer"
    if isinstance(value, float):
        return "Float"
    return "String"


def normalize_parameter_groups(entity: dict[str, Any]) -> None:
    for group_name, group in entity.items():
        if group_name.endswith("P") and isinstance(group, dict):
            group.setdefault("id", f"{entity['id']}/{group_name}")
            if isinstance(group.get("alias"), str):
                group["alias"] = [group["alias"]]


def apply_bta_kind_rules(components: list[dict[str, Any]]) -> None:
    """Specialize generic PALS device kinds using BtA naming conventions."""
    for component in components:
        name = local_name(component["id"])
        for rule in BTA_KIND_RULES:
            name_pattern = rule.get("name_pattern")
            matches = name in rule.get("names", ()) or (
                name_pattern is not None
                and re.match(name_pattern, name, flags=re.IGNORECASE) is not None
            )
            if not matches:
                continue
            if component["kind"] != rule["source_kind"]:
                raise ValueError(
                    f"BtA kind rule for {name} expects {rule['source_kind']}, "
                    f"found {component['kind']}"
                )
            component["kind"] = rule["target_kind"]
            component["functions"] = default_functions(rule["target_kind"])
            break


def add_multiwire_device_info(components: list[dict[str, Any]]) -> None:
    """Add BtA-specific multiwire native type and construction metadata."""
    for component in components:
        name = local_name(component["id"])
        device_info = MW_DEVICE_INFO["devices"].get(name)
        if device_info is None:
            continue
        native_type = MW_DEVICE_INFO["native_type"]
        if native_type not in component["native_types"]:
            component["native_types"].append(native_type)
        meta = component.setdefault("MetaP", {})
        meta.setdefault("description", MW_DEVICE_INFO["description"])
        existing_keys = {
            item.get("key")
            for item in meta.setdefault("additional_metadata", [])
            if isinstance(item, dict)
        }
        meta["additional_metadata"].extend(
            {
                "key": key,
                "value": str(value),
                "datatype": metadata_datatype(value),
            }
            for key, value in device_info.items()
            if key not in existing_keys
        )
        normalize_parameter_groups(component)


def resolve_ado_name(name: str, rules: list[tuple[str, tuple[str, str]]]) -> str | None:
    for pattern, (device_template, attribute) in rules:
        match = re.match(pattern, name, flags=re.IGNORECASE)
        if match:
            return f"{match.expand(device_template)}:{attribute}"
    return None


def generate_ado_signals(
    components: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Generate deduplicated ADO signals and component bindings."""
    signals_by_id: dict[str, dict[str, Any]] = {}
    bindings: list[dict[str, Any]] = []

    for component in components:
        component_rules = ADO_RULES.get(component["kind"])
        if component_rules is None:
            continue
        name = local_name(component["id"])

        for semantic_name, rules in component_rules.items():
            ado_name = resolve_ado_name(name, rules)
            if ado_name is None:
                continue
            spec = ADO_SIGNAL_SPECS[semantic_name]
            signal_id = f"inst:{ado_name}"
            signal = {
                **ADO_SIGNAL_DEFAULTS,
                "id": signal_id,
                "signal_role": spec["signal_role"],
                "native_description": spec["native_description"],
                "canonical_signal_type": spec["canonical_signal_type"],
                "quantity_kind": spec["quantity_kind"],
                "native_data_type": spec["native_data_type"],
                "native_unit": spec["native_unit"],
                "alias": [semantic_name],
            }
            if "MetaP" in spec:
                signal["MetaP"] = deepcopy(spec["MetaP"])
            normalize_parameter_groups(signal)

            existing = signals_by_id.setdefault(signal_id, signal)
            if existing != signal:
                raise ValueError(f"conflicting definitions generated for signal {signal_id}")
            bindings.append(
                {
                    "id": f"{component['id']}.{semantic_name}_binding",
                    "subject": component["id"],
                    "predicate": spec["predicate"],
                    "object": signal_id,
                }
            )

    return list(signals_by_id.values()), bindings


def enrich_document(skeleton: dict[str, Any]) -> dict[str, Any]:
    """Return a BtA-enriched copy of a signal-free NARAD skeleton."""
    document = deepcopy(skeleton)
    facility = document["facility"]
    if facility.get("signals") or facility.get("signal_bindings"):
        raise ValueError("expected a skeleton with empty signals and signal_bindings")

    apply_bta_kind_rules(facility["components"])
    add_multiwire_device_info(facility["components"])
    signals, bindings = generate_ado_signals(facility["components"])
    facility["signals"] = signals
    facility["signal_bindings"] = bindings
    facility.setdefault("identifiers", []).extend(
        deepcopy(BTA_DOCUMENT_ENRICHMENT["facility_identifiers"])
    )
    document["description"] = BTA_DOCUMENT_ENRICHMENT["description"]
    document.setdefault("notes", []).extend(BTA_DOCUMENT_ENRICHMENT["notes"])
    validated = narad_model.PALSAccelerator.model_validate(document)
    return validated.model_dump(mode="json", exclude_none=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("-help", action="help", help="show this help message and exit")
    parser.add_argument(
        "-input",
        "--input",
        type=Path,
        default=DEFAULT_INPUT,
        metavar="INPUT_SKELETON_YAML",
        help=f"signal-free NARAD skeleton to enrich (default: {DEFAULT_INPUT.name})",
    )
    parser.add_argument(
        "-output",
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        metavar="OUTPUT_NARAD_YAML",
        help=f"enriched NARAD YAML file to create (default: {DEFAULT_OUTPUT.name})",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    with args.input.open(encoding="utf-8") as stream:
        skeleton = yaml.safe_load(stream)
    document = enrich_document(skeleton)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as stream:
        yaml.safe_dump(document, stream, sort_keys=False, allow_unicode=True, width=100)
    facility = document["facility"]
    print(
        f"Wrote {args.output} with {len(facility['signals'])} ADO signals and "
        f"{len(facility['signal_bindings'])} signal bindings."
    )


if __name__ == "__main__":
    main()
