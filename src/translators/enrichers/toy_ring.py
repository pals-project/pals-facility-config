#!/usr/bin/env python3
"""Enrich the hypothetical EIC toy ring with fictional EPICS PVs.

Usage: python toy_ring.py -input INPUT_SKELETON_YAML -output OUTPUT_NARAD_YAML
All device naming and signal semantics are configured below.
"""

from __future__ import annotations

import argparse
from copy import deepcopy
from pathlib import Path
import re
from typing import Any

import yaml

from narad.datamodel import narad_pydantic as narad_model
from translators.final_instance import initialize_final_instance
from translators.palsparserpy_to_narad import component_functions
from translators.yaml_order import order_document_components


REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_INPUT = REPO_ROOT / ".local/translation/skeletons/toy_ring_narad_skeleton_palsparserpy.yaml"
DEFAULT_OUTPUT = REPO_ROOT / "examples/toy_ring_narad_instance.yaml"

TOY_RING_KIND_RULES = (
    {"name_pattern": r"ES[0-9]+_BPM[0-9]+", "source_kind": "DiagnosticDevice",
     "target_kind": "BeamPositionMonitor"},
)

# Full element-name matches; lowercase PV device names, uppercase field suffixes.
# Each toy corrector has independent H and V supplies bound to the same component.
EPICS_RULES = {
    "Kicker": {
        f"{plane_name}_{semantic}": [(r"(es[0-9]+)_t([0-9]+)", rf"\1-t\2:PS:{plane}:{suffix}")]
        for plane_name, plane in (("horizontal", "H"), ("vertical", "V"))
        for semantic, suffix in (("magnet_status", "Status"),
                                 ("current_setpoint", "Current-SP"),
                                 ("current_readback", "Current-RB"),
                                 ("current_min", "Current-SP.DRVL"),
                                 ("current_max", "Current-SP.DRVH"))
    },
    "BeamPositionMonitor": {
        "horizontal_position": [(r"(es[0-9]+)_bpm([0-9]+)", r"\1-bpm\2:X-RB")],
        "vertical_position": [(r"(es[0-9]+)_bpm([0-9]+)", r"\1-bpm\2:Y-RB")],
    },
}

EPICS_SIGNAL_SPECS = {
    "current_min": {
        "signal_role": "RangeLimit", "native_description": "Minimum allowed current setpoint.",
        "canonical_signal_type": "MagnetCurrentRange", "quantity_kind": "ElectricCurrent",
        "native_data_type": "Float", "native_unit": "A", "predicate": "HasLimitSignal",
    },
    "current_max": {
        "signal_role": "RangeLimit", "native_description": "Maximum allowed current setpoint.",
        "canonical_signal_type": "MagnetCurrentRange", "quantity_kind": "ElectricCurrent",
        "native_data_type": "Float", "native_unit": "A", "predicate": "HasLimitSignal",
    },
    "current_setpoint": {
        "signal_role": "Setpoint", "native_description": "Desired magnet current command.",
        "canonical_signal_type": "MagnetCurrentSetpoint", "quantity_kind": "ElectricCurrent",
        "native_data_type": "Float", "native_unit": "A", "predicate": "HasSetpointSignal",
    },
    "current_readback": {
        "signal_role": "Readback", "native_description": "Measured magnet current.",
        "canonical_signal_type": "MagnetCurrentReadback", "quantity_kind": "ElectricCurrent",
        "native_data_type": "Float", "native_unit": "A", "predicate": "HasReadbackSignal",
    },
    "magnet_status": {
        "signal_role": "Status", "native_description": "Power-supply or device state summary.",
        "canonical_signal_type": "Status", "quantity_kind": "State",
        "native_data_type": "String", "native_unit": "none", "predicate": "HasSignal",
    },
    "horizontal_position": {
        "signal_role": "Readback", "native_description": "Measured horizontal beam position.",
        "canonical_signal_type": "HorizontalBeamPosition", "quantity_kind": "BeamPosition",
        "native_data_type": "Float", "native_unit": "mm", "predicate": "HasReadbackSignal",
    },
    "vertical_position": {
        "signal_role": "Readback", "native_description": "Measured vertical beam position.",
        "canonical_signal_type": "VerticalBeamPosition", "quantity_kind": "BeamPosition",
        "native_data_type": "Float", "native_unit": "mm", "predicate": "HasReadbackSignal",
    },
}

EPICS_SIGNAL_DEFAULTS = {
    "kind": "Signal",
    "source_system": "EPICS",
    "access_protocol": "EPICS PVAccess",
}

TOY_RING_DOCUMENT_ENRICHMENT = {
    "facility_identifiers": [{"identifier_type": "LOCAL", "identifier_value": "EIC_TOY_RING"}],
    "description": "Hypothetical EIC toy ring enriched with fictional EPICS controls.",
    "initial_change_summary": (
        "Initial toy-ring NARAD instance generated from PALS and enriched with "
        "fictional EPICS signal metadata."
    ),
    "notes": ["EPICS PV names are made up for this example; they do not describe operational EIC controls."],
}


def local_name(identifier: str) -> str:
    return identifier.removeprefix("inst:")


def default_functions(kind: str) -> list[str]:
    """Read a component kind's nearest PALS translation default."""
    model = getattr(narad_model, kind)
    functions = component_functions(model)
    if functions is None:
        raise ValueError(f"NARAD component kind {kind} has no translation default")
    return functions


def normalize_parameter_groups(entity: dict[str, Any]) -> None:
    for group_name, group in entity.items():
        if group_name.endswith("P") and isinstance(group, dict):
            group.setdefault("id", f"{entity['id']}/{group_name}")
            if isinstance(group.get("alias"), str):
                group["alias"] = [group["alias"]]


def device_name(component: dict[str, Any]) -> str:
    """Strip only the occurrence suffix added during lattice expansion."""
    return re.sub(r"_\d{3}$", "", local_name(component["id"]))


def apply_toy_ring_kind_rules(components: list[dict[str, Any]]) -> None:
    """Specialize PALS device kinds using the first matching toy-ring rule."""
    for component in components:
        name = device_name(component)
        for rule in TOY_RING_KIND_RULES:
            name_pattern = rule.get("name_pattern")
            matches = name in rule.get("names", ()) or (
                name_pattern is not None
                and re.fullmatch(name_pattern, name, flags=re.IGNORECASE) is not None
            )
            if not matches:
                continue
            if component["kind"] not in {rule["source_kind"], rule["target_kind"]}:
                raise ValueError(
                    f"Toy-ring kind rule for {name} expects {rule['source_kind']} or "
                    f"{rule['target_kind']}, found {component['kind']}"
                )
            component["kind"] = rule["target_kind"]
            component["functions"] = default_functions(rule["target_kind"])
            break


def resolve_epics_names(component: dict[str, Any]) -> dict[str, str]:
    """Resolve the first full-name matching rule for each configured signal."""
    names = {}
    for semantic, rules in EPICS_RULES.get(component["kind"], {}).items():
        for pattern, template in rules:
            match = re.fullmatch(pattern, device_name(component).lower())
            if match:
                names[semantic] = match.expand(template)
                break
    return names


def generate_epics_signals(
    components: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Generate deduplicated EPICS signals and component bindings."""
    signals_by_id: dict[str, dict[str, Any]] = {}
    bindings: list[dict[str, Any]] = []

    for component in components:
        for semantic_name, epics_name in resolve_epics_names(component).items():
            base_semantic = semantic_name
            for plane in ("horizontal", "vertical"):
                if semantic_name.startswith(f"{plane}_") and semantic_name != f"{plane}_position":
                    base_semantic = semantic_name.removeprefix(f"{plane}_")
                    break
            spec = EPICS_SIGNAL_SPECS[base_semantic]
            signal_id = f"inst:{epics_name}"
            signal = {
                **EPICS_SIGNAL_DEFAULTS,
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


def enrich_document(
    skeleton: dict[str, Any], existing_document: dict[str, Any] | None = None
) -> dict[str, Any]:
    """Return a toy-ring-enriched copy of a signal-free NARAD skeleton."""
    document = deepcopy(skeleton)
    facility = document["facility"]
    if facility.get("signals") or facility.get("signal_bindings"):
        raise ValueError("expected a skeleton with empty signals and signal_bindings")

    apply_toy_ring_kind_rules(facility["components"])
    signals, bindings = generate_epics_signals(facility["components"])
    facility["signals"] = signals
    facility["signal_bindings"] = bindings
    facility.setdefault("identifiers", []).extend(
        deepcopy(TOY_RING_DOCUMENT_ENRICHMENT["facility_identifiers"])
    )
    document["description"] = TOY_RING_DOCUMENT_ENRICHMENT["description"]
    document.setdefault("notes", []).extend(TOY_RING_DOCUMENT_ENRICHMENT["notes"])
    initialize_final_instance(
        document,
        summary=TOY_RING_DOCUMENT_ENRICHMENT["initial_change_summary"],
        existing_document=existing_document,
    )
    validated = narad_model.PALSAccelerator.model_validate(document)
    return order_document_components(
        validated.model_dump(mode="json", exclude_none=True)
    )


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
    existing_document = None
    if args.output.exists():
        with args.output.open(encoding="utf-8") as stream:
            existing_document = yaml.safe_load(stream)
    document = enrich_document(skeleton, existing_document)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as stream:
        yaml.safe_dump(document, stream, sort_keys=False, allow_unicode=True, width=100)
    facility = document["facility"]
    print(
        f"Wrote {args.output} with {len(facility['signals'])} EPICS signals and "
        f"{len(facility['signal_bindings'])} signal bindings."
    )


if __name__ == "__main__":
    main()
