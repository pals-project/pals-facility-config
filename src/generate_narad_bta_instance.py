#!/usr/bin/env python3
"""Create an accelerator-core NARAD instance from PALS and local ADO rules."""

from __future__ import annotations

import argparse
from collections import Counter
from copy import deepcopy
import re
from pathlib import Path
from typing import Any

import yaml


DEFAULT_INPUT = Path(__file__).with_name("bta.pals.yaml")
DEFAULT_OUTPUT = Path(__file__).with_name("narad_bta_instance.yaml")

MAGNET_FUNCTIONS = {
    "Bend": ["Steering"],
    "Quadrupole": ["Focusing"],
    "Sextupole": ["Focusing"],
    "Kicker": ["Steering"],
}
DIRECT_PARAMETER_GROUPS = ("ReferenceP", "TwissP", "BodyShiftP")


# BtA multiwire monitor device properties used to populate additional_metadata fields.
MW_DEVICE_INFO = {
    "MW006": {
        "nbr_wires_x": 32,
        "nbr_wires_y": 32,
        "spacing_x": 0.0015,
        "spacing_y": 0.0015,
    },
    "MW060": {
        "nbr_wires_x": 32,
        "nbr_wires_y": 32,
        "spacing_x": 0.0025,
        "spacing_y": 0.0025,
    },
    "MW125": {
        "nbr_wires_x": 32,
        "nbr_wires_y": 32,
        "spacing_x": 0.0025,
        "spacing_y": 0.0025,
    },
    "MW166": {
        "nbr_wires_x": 32,
        "nbr_wires_y": 32,
        "spacing_x": 0.0025,
        "spacing_y": 0.0025,
    },
    "MWA15": {
        "nbr_wires_x": 64,
        "nbr_wires_y": 32,
        "spacing_x": 0.002,
        "spacing_y": 0.002,
    },
}

# ADO signal generation rules for BtA components. 
# Each entry maps a PALS element name pattern to an ADO device and attribute.
ADO_RULES = {
        'BTA': {#System
            'Quadrupole': {#Kind
                'current_setpoint':  [(r"QH0*([1-9][0-9]*)", (r"bta-qf\1-ps", "setpointS")),
                              (r"QV0*([1-9][0-9]*)", (r"bta-qd\1-ps", "setpointS"))],
                'current_readback':  [(r"QH0*([1-9][0-9]*)", (r"bta-qf\1-ps", "currentM")),
                              (r"QV0*([1-9][0-9]*)", (r"bta-qd\1-ps", "currentM"))],
                'current_range':     [(r"QH0*([1-9][0-9]*)", (r"bta-qf\1-ps", "rangeC")),
                              (r"QV0*([1-9][0-9]*)", (r"bta-qd\1-ps", "rangeC"))],
                'magnet_status':            [(r"QH0*([1-9][0-9]*)", (r"bta-qf\1-ps", "stateS")),
                              (r"QV0*([1-9][0-9]*)", (r"bta-qd\1-ps", "stateS"))],
            },
            'Kicker':{#Kind
                'current_setpoint': [(r"DV0*([1-9][0-9]*)", (r"bta-tv\1-ps", "setpointS")),
                                     (r"DH0*([1-9][0-9]*)", (r"bta-th\1-ps", "setpointS"))],
                'current_readback': [(r"DV0*([1-9][0-9]*)", (r"bta-tv\1-ps", "currentM")),
                                     (r"DH0*([1-9][0-9]*)", (r"bta-th\1-ps", "currentM"))],
                'current_range': [(r"DV0*([1-9][0-9]*)", (r"bta-tv\1-ps", "rangeC")),
                                  (r"DH0*([1-9][0-9]*)", (r"bta-th\1-ps", "rangeC"))],
                'magnet_status': [(r"DV0*([1-9][0-9]*)", (r"bta-tv\1-ps", "stateS")),
                           (r"DH0*([1-9][0-9]*)", (r"bta-th\1-ps", "stateS"))],
            },
            'BeamProfileMonitor':{#Kind
                'horizontal_profile': [(r"MWA([0-9]+)", (r"adrA\1MWCntl", "horInDataM")),
                                       (r"MW([0-9]+)",  (r"btaMW\1Cntl",  "horInDataM"))],
                'vertical_profile': [(r"MWA([0-9]+)", (r"adrA\1MWCntl", "verInDataM")),
                                        (r"MW([0-9]+)",  (r"btaMW\1Cntl",  "verInDataM"))],
                'insertion_status': [(r"MWA([0-9]+)", (r"adrA\1MWCntl", "harpIsM")),
                                     (r"MW([0-9]+)",  (r"btaMW\1Cntl",  "harpIsM"))]
            }
        }
    }

# ADO signal specifications for BtA components. 
# Each entry defines the properties of a signal type.
ADO_SIGNAL_SPECS = {
    "current_setpoint": {
        "signal_role": "Setpoint",
        "native_description": "Desired magnet current command.",
        "canonical_signal_type": "MagnetCurrentSetpoint",
        "quantity_kind": "ElectricCurrent",
        "native_data_type": "Float",
        "native_unit": "A",
        "predicate": "pals:has_setpoint_signal",
    },
    "current_readback": {
        "signal_role": "Readback",
        "native_description": "Measured magnet current.",
        "canonical_signal_type": "MagnetCurrentReadback",
        "quantity_kind": "ElectricCurrent",
        "native_data_type": "Float",
        "native_unit": "A",
        "predicate": "pals:has_readback_signal",
    },
    "current_range": {
        "signal_role": "RangeLimit",
        "native_description": "Allowed magnet-current range returned as [maximum, minimum].",
        "canonical_signal_type": "MagnetCurrentRange",
        "quantity_kind": "ElectricCurrent",
        "native_data_type": "FloatArray",
        "native_unit": "A",
        "predicate": "pals:has_limit_signal",
        "MetaP": {
            "additional_metadata": [
                {"key": "array_order", "value": "maximum,minimum", "datatype": "String"},
                {"key": "array_length", "value": "2", "datatype": "Integer"},
            ]
        },
    },
    "magnet_status": {
        "signal_role": "Status",
        "native_description": "Power-supply or device state summary.",
        "canonical_signal_type": "Status",
        "quantity_kind": "State",
        "native_data_type": "String",
        "native_unit": "none",
        "predicate": "pals:has_signal",
    },
    "horizontal_profile": {
        "signal_role": "Readback",
        "native_description": "Measured horizontal multiwire beam-intensity profile.",
        "canonical_signal_type": "HorizontalBeamPosition",
        "quantity_kind": "BeamPosition",
        "native_data_type": "FloatArray",
        "native_unit": "V",
        "predicate": "pals:has_readback_signal",
    },
    "vertical_profile": {
        "signal_role": "Readback",
        "native_description": "Measured vertical multiwire beam-intensity profile.",
        "canonical_signal_type": "VerticalBeamPosition",
        "quantity_kind": "BeamPosition",
        "native_data_type": "FloatArray",
        "native_unit": "V",
        "predicate": "pals:has_readback_signal",
    },
    "insertion_status": {
        "signal_role": "Status",
        "native_description": "Insertion status of the multiwire monitor.",
        "canonical_signal_type": "Status",
        "quantity_kind": "State",
        "native_data_type": "String",
        "native_unit": "none",
        "predicate": "pals:has_signal",
    },
}


def metadata_datatype(value: Any) -> str:
    """Return the schema datatype name for an additional-metadata value."""
    if isinstance(value, bool):
        return "Boolean"
    if isinstance(value, int):
        return "Integer"
    if isinstance(value, float):
        return "Float"
    return "String"


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


def add_mw_metadata(component: dict[str, Any], name: str) -> None:
    """Add configured multiwire properties without replacing source MetaP fields."""
    device_info = MW_DEVICE_INFO.get(name.upper())
    if device_info is None:
        return

    meta = component.setdefault("MetaP", {})
    meta.setdefault("description", "Multiwire beam-profile monitor.")
    additional_metadata = meta.setdefault("additional_metadata", [])
    existing_keys = {
        item.get("key") for item in additional_metadata if isinstance(item, dict)
    }
    additional_metadata.extend(
        {
            "key": key,
            "value": str(value),
            "datatype": metadata_datatype(value),
        }
        for key, value in device_info.items()
        if key not in existing_keys
    )


def resolve_ado_name(name: str, rules: list[tuple[str, tuple[str, str]]]) -> str | None:
    """Resolve an element name to an ADO device and attribute using regex rules."""
    for pattern, (device_template, attribute) in rules:
        match = re.match(pattern, name, flags=re.IGNORECASE)
        if match:
            return f"{match.expand(device_template)}:{attribute}"
    return None


def generate_ado_signals(
    components_by_name: dict[str, dict[str, Any]], system: str = "BTA"
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Generate deduplicated ADO signals and per-component signal bindings."""
    system_rules = ADO_RULES[system]
    signals_by_id: dict[str, dict[str, Any]] = {}
    bindings: list[dict[str, Any]] = []

    for name, component in components_by_name.items():
        component_rules = system_rules.get(component["kind"])
        if component_rules is None:
            continue

        for semantic_name, rules in component_rules.items():
            ado_name = resolve_ado_name(name, rules)
            if ado_name is None:
                continue

            spec = ADO_SIGNAL_SPECS[semantic_name]
            signal_id = f"inst:{ado_name}"
            signal = {
                "id": signal_id,
                "kind": "Signal",
                "signal_role": spec["signal_role"],
                "source_system": "Other",
                "native_description": spec["native_description"],
                "canonical_signal_type": spec["canonical_signal_type"],
                "quantity_kind": spec["quantity_kind"],
                "native_data_type": spec["native_data_type"],
                "native_unit": spec["native_unit"],
                "access_protocol": "ADO",
                "alias": [semantic_name],
            }
            if "MetaP" in spec:
                signal["MetaP"] = deepcopy(spec["MetaP"])
            normalize_parameter_groups(signal)

            existing = signals_by_id.setdefault(signal_id, signal)
            if existing != signal:
                raise ValueError(f"conflicting definitions generated for signal {signal_id}")

            component_id = component["id"]
            bindings.append(
                {
                    "id": f"{component_id}.{semantic_name}_binding",
                    "subject": component_id,
                    "predicate": spec["predicate"],
                    "object": signal_id,
                }
            )

    return list(signals_by_id.values()), bindings


def instance_id(name: str) -> str:
    """Return a stable local instance CURIE."""
    return f"inst:{name.upper()}"


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
    """Return a list of native type identifiers for a PALS element."""
    values = [str(source["kind"])]
    bmad_key = source.get("Bmad", {}).get("Bmad_key")
    if bmad_key and bmad_key not in values:
        values.append(str(bmad_key))
    return values


def component_from_pals(name: str, source: dict[str, Any]) -> dict[str, Any] | None:
    """Map a PALS element to a concrete class in the current NARAD schema."""
    source_kind = source.get("kind")
    target_kind = source_kind
    functions: list[str]

    if source_kind in MAGNET_FUNCTIONS:
        functions = list(MAGNET_FUNCTIONS[source_kind])
    elif source_kind == "Instrument":
        target_kind = "BeamPositionMonitor"
        functions = ["BeamPositionMeasurement"]
    elif source_kind == "Marker" and name.lower().startswith("mw"):
        target_kind = "BeamProfileMonitor"
        functions = ["BeamProfileMeasurement"]
    elif source_kind == "BeginningEle":
        target_kind = "BeginningEle"
        functions = ["Mark"]
    elif source_kind == "Drift":
        target_kind = "Drift"
        functions = ["DriftSpace"]
    elif source_kind == "Marker":
        target_kind = "Marker"
        functions = ["Mark"]
    else:
        # Controller, Lattice, BeamLine, and constants have no direct
        # component representation in the current accelerator-core schema.
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
            component[group_name] = source[group_name]

    if source.get("MetaP"):
        component["MetaP"] = deepcopy(source["MetaP"])

    if target_kind == "BeamProfileMonitor":
        add_mw_metadata(component, name)

    if source.get("BendP"):
        component["BendP"] = dict(source["BendP"])

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


def load_facility_records(path: Path) -> tuple[dict[str, dict[str, Any]], list[str], bool]:
    """Load PALS facility records and extract the beamline definition."""
    with path.open(encoding="utf-8") as stream:
        document = yaml.safe_load(stream)

    try:
        records = document["PALS"]["facility"]
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
    if len(beamlines) != 1:
        raise ValueError(f"expected exactly one BeamLine, found {len(beamlines)}")
    _, beamline = beamlines[0]
    return named, list(beamline.get("line", [])), bool(beamline.get("periodic", False))


def build_document(source_path: Path) -> dict[str, Any]:
    """Build a NARAD instance document from a PALS export and local ADO rules."""
    records, line, periodic = load_facility_records(source_path)
    components_by_name = {
        name: component
        for name, source in records.items()
        if (component := component_from_pals(name, source)) is not None
    }
    signals, signal_bindings = generate_ado_signals(components_by_name)

    retained_line = [name for name in line if name in components_by_name]
    occurrence_totals = Counter(retained_line)
    occurrence_numbers: Counter[str] = Counter()
    components = []
    ordered_ids = []
    for name in retained_line:
        component = deepcopy(components_by_name[name])
        if occurrence_totals[name] > 1:
            occurrence_numbers[name] += 1
            component["id"] = instance_id(f"{name}_{occurrence_numbers[name]:03d}")
            normalize_parameter_groups(component, replace_ids=True)
        components.append(component)
        ordered_ids.append(component["id"])

    # Retain supported records that are definitions but are not used by this line.
    line_names = set(retained_line)
    components.extend(
        component for name, component in components_by_name.items() if name not in line_names
    )

    beamline_id = instance_id("BTA_LINE")
    relations = []
    for subject, obj in zip(ordered_ids, ordered_ids[1:]):
        relations.append(
            {
                "id": f"inst:{subject[5:]}_PRECEDES_{obj[5:]}",
                "subject": subject,
                "predicate": "pals:precedes",
                "object": obj,
                "context": "beamline_order",
                "beamline_context": beamline_id,
            }
        )

    return {
        "description": "Skeleton NARAD representation of the BTA beamline generated from bta.pals.yaml.",
        "kind": "PALSAccelerator",
        "version": "0.1.0",
        "notes": [
            "Generated from a PALS lattice export and enriched with ADO signals defined by local naming rules.",
            "Model-only drifts, controllers, constants, and lattice records are omitted because the current accelerator-core schema has no direct representation for them.",
        ],
        "facility": {
            "identifiers": [
                {"identifier_type": "LOCAL", "identifier_value": "BTA"}
            ],
            "components": components,
            "beamlines": [
                {
                    "id": beamline_id,
                    "kind": "BeamLine",
                    "functions": ["BeamLineSection"],
                    "beamline_relation": "Inline",
                    "multipass": False,
                    "periodic": periodic,
                    "description": "BTA beamline imported from bta.pals.yaml.",
                }
            ],
            "signals": signals,
            "signal_bindings": signal_bindings,
            "component_relations": relations,
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("output", nargs="?", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    document = build_document(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as stream:
        yaml.safe_dump(document, stream, sort_keys=False, allow_unicode=True, width=100)
    facility = document["facility"]
    print(
        f"Wrote {args.output} with {len(facility['components'])} components and "
        f"{len(facility['component_relations'])} beamline-order relations, "
        f"{len(facility['signals'])} signals, and "
        f"{len(facility['signal_bindings'])} signal bindings."
    )


if __name__ == "__main__":
    main()
