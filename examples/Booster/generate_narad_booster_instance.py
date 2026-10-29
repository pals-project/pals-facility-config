#!/usr/bin/env python3
"""Enrich a control-neutral NARAD skeleton with Booster BPM and corrector ADO data.

Usage: python generate_narad_booster_instance.py -input INPUT_SKELETON_YAML -output OUTPUT_NARAD_YAML
Run ``python generate_narad_booster_instance.py -help`` for option details.
"""

from __future__ import annotations

import argparse
from copy import deepcopy
from pathlib import Path
import re
from typing import Any, Callable

import yaml

from narad.datamodel import narad_pydantic as narad_model
from narad_system.schema.yaml_order import order_document_components


DEFAULT_INPUT = Path(__file__).with_name("booster_narad_skeleton_palsparserpy.yaml")
DEFAULT_OUTPUT = Path(__file__).with_name("booster_narad_instance.yaml")

BOOSTER_KIND_RULES = (
    {
        "name_pattern": r"PUE[HV][A-F][1-8]",
        "source_kind": "DiagnosticDevice",
        "target_kind": "BeamPositionMonitor",
    },
)

def corrector_ado_device(match: re.Match[str]) -> str:
    """Keep power-supply device names lowercase regardless of element casing."""
    plane, sector, number = match.groups()
    return f"b{sector.lower()}{number}-t{plane.lower()}-ps"


def backleg_ado_device(match: re.Match[str]) -> str:
    """Map an extraction-bump dipole to its dedicated backleg supply."""
    return f"Booster.b{match.group(1).lower()}-blw-ps"


# Each signal has ordered (element pattern, (device, attribute)) rules, as in
# the BtA generator. Templates support regex backreferences; a callable can
# format a match when the native device name requires case conversion.
AdoTemplate = str | Callable[[re.Match[str]], str]
ADO_RULES = {
    "BeamPositionMonitor": {
        "horizontal_position": [
            (r"PUEH([A-F])([1-8])", ("orbitData.booster", r"horPos\1\2M")),
        ],
        "vertical_position": [
            (r"PUEV([A-F])([1-8])", ("orbitData.booster", r"verPos\1\2M")),
        ],
    },
    "Kicker": {
        "magnet_status": [(r"D([HV])C([A-F])([1-8])", (corrector_ado_device, "stateS"))],
        "current_range": [(r"D([HV])C([A-F])([1-8])", (corrector_ado_device, "rangeC"))],
        "current_setpoint": [(r"D([HV])C([A-F])([1-8])", (corrector_ado_device, "setpointsM"))],
        "current_readback": [(r"D([HV])C([A-F])([1-8])", (corrector_ado_device, "currentM"))],
    },
    # Series quadrupoles share one set of supply signals per plane.
    "Quadrupole": {
        "magnet_status": [
            (r"QH[A-F][1-8]", ("b-qtrimh-ps", "stateS")),
            (r"QV[A-F][1-8]", ("b-qtrimv-ps", "stateS")),
        ],
        "current_range": [
            (r"QH[A-F][1-8]", ("b-qtrimh-ps", "rangeC")),
            (r"QV[A-F][1-8]", ("b-qtrimv-ps", "rangeC")),
        ],
        "current_setpoint": [
            (r"QH[A-F][1-8]", ("b-qtrimh-ps", "setpointsAvgM")),
            (r"QV[A-F][1-8]", ("b-qtrimv-ps", "setpointsAvgM")),
        ],
        "current_readback": [
            (r"QH[A-F][1-8]", ("b-qtrimh-ps", "currentAvgM")),
            (r"QV[A-F][1-8]", ("b-qtrimv-ps", "currentAvgM")),
        ],
        "main_magnet_status": [(r"Q[HV][A-F][1-8]", ("bmm.control", "stateM"))],
        "main_current_range": [(r"Q[HV][A-F][1-8]", ("bmm.control", "currentRangeC"))],
        "main_current_setpoint": [(r"Q[HV][A-F][1-8]", ("bmm.control", "psiCurrentSetpointAvgM"))],
        "main_current_readback": [(r"Q[HV][A-F][1-8]", ("bmm.control", "dcctCurrentOutputAvgM"))],
    },
    # Series sextupoles share one chromaticity supply per plane.
    "Sextupole": {
        "magnet_status": [
            (r"SH[A-F][1-8]", ("Booster.b-chromh-ps", "stateS")),
            (r"SV[A-F][1-8]", ("Booster.b-chromv-ps", "stateS")),
        ],
        "current_range": [
            (r"SH[A-F][1-8]", ("Booster.b-chromh-ps", "rangeC")),
            (r"SV[A-F][1-8]", ("Booster.b-chromv-ps", "rangeC")),
        ],
        "current_setpoint": [
            (r"SH[A-F][1-8]", ("Booster.b-chromh-ps", "setpointsAvgM")),
            (r"SV[A-F][1-8]", ("Booster.b-chromv-ps", "setpointsAvgM")),
        ],
        "current_readback": [
            (r"SH[A-F][1-8]", ("Booster.b-chromh-ps", "currentAvgM")),
            (r"SV[A-F][1-8]", ("Booster.b-chromv-ps", "currentAvgM")),
        ],
        "stopband_magnet_status": [
            (r"SH(?:C8|F8)", ("b-sxr1-ps", "stateS")),
            (r"SH(?:B4|E4)", ("b-sxr2-ps", "stateS")),
        ],
        "stopband_current_range": [
            (r"SH(?:C8|F8)", ("b-sxr1-ps", "rangeC")),
            (r"SH(?:B4|E4)", ("b-sxr2-ps", "rangeC")),
        ],
        "stopband_current_setpoint": [
            (r"SH(?:C8|F8)", ("b-sxr1-ps", "setpointsAvgM")),
            (r"SH(?:B4|E4)", ("b-sxr2-ps", "setpointsAvgM")),
        ],
        "stopband_current_readback": [
            (r"SH(?:C8|F8)", ("b-sxr1-ps", "currentAvgM")),
            (r"SH(?:B4|E4)", ("b-sxr2-ps", "currentAvgM")),
        ],
    },
    "Bend": {
        "magnet_status": [
            (r"DH[A-F][1-8]", ("bmm.control", "stateM")),
        ],
        "current_range": [
            (r"DH[A-F][1-8]", ("bmm.control", "currentRangeC")),
        ],
        "current_setpoint": [
            (r"DH[A-F][1-8]", ("bmm.control", "psiCurrentSetpointAvgM")),
        ],
        "current_readback": [
            (r"DH[A-F][1-8]", ("bmm.control", "dcctCurrentOutputAvgM")),
        ],
        "backleg_magnet_status": [
            (r"DH(C7|D1|D4|D7|E1)", (backleg_ado_device, "stateS")),
        ],
        "backleg_current_range": [
            (r"DH(C7|D1|D4|D7|E1)", (backleg_ado_device, "rangeC")),
        ],
        "backleg_current_setpoint": [
            (r"DH(C7|D1|D4|D7|E1)", (backleg_ado_device, "setpointsAvgM")),
        ],
        "backleg_current_readback": [
            (r"DH(C7|D1|D4|D7|E1)", (backleg_ado_device, "currentAvgM")),
        ],
    },
}

# Supply-specific wiring signs only; no current-to-strength conversion is applied.
# Add a rule with a component kind, full-name pattern, supply role, and polarity.
POLARITY_RULES = {
    "stopband_sxr1_positive": {
        "kind": "Sextupole", "name_pattern": r"SHC8",
        "role": "stopband", "supply": "b-sxr1-ps", "polarity": 1,
        "metadata": {"stopband_purpose": "13/3 extraction"},
    },
    "stopband_sxr1_negative": {
        "kind": "Sextupole", "name_pattern": r"SHF8",
        "role": "stopband", "supply": "b-sxr1-ps", "polarity": -1,
        "metadata": {"stopband_purpose": "13/3 extraction"},
    },
    "stopband_sxr2_negative": {
        "kind": "Sextupole", "name_pattern": r"SHB4",
        "role": "stopband", "supply": "b-sxr2-ps", "polarity": -1,
        "metadata": {"stopband_purpose": "13/3 extraction"},
    },
    "stopband_sxr2_positive": {
        "kind": "Sextupole", "name_pattern": r"SHE4",
        "role": "stopband", "supply": "b-sxr2-ps", "polarity": 1,
        "metadata": {"stopband_purpose": "13/3 extraction"},
    },
    "horizontal_tune_quad": {
        "kind": "Quadrupole", "name_pattern": r"QH[A-F][1-8]",
        "role": "trim", "supply": "b-qtrimh-ps", "polarity": 1,
        "metadata": {"main_supply": "bmm.control"},
    },
    "vertical_tune_quad": {
        "kind": "Quadrupole", "name_pattern": r"QV[A-F][1-8]",
        "role": "trim", "supply": "b-qtrimv-ps", "polarity": -1,
        "metadata": {"main_supply": "bmm.control"},
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
    "horizontal_position": {
        "signal_role": "Readback", "native_description": "Measured horizontal beam position.",
        "canonical_signal_type": "HorizontalBeamPosition", "quantity_kind": "BeamPosition",
        "native_data_type": "Float", "native_unit": "mm", "predicate": "pals:has_readback_signal",
    },
    "vertical_position": {
        "signal_role": "Readback", "native_description": "Measured vertical beam position.",
        "canonical_signal_type": "VerticalBeamPosition", "quantity_kind": "BeamPosition",
        "native_data_type": "Float", "native_unit": "mm", "predicate": "pals:has_readback_signal",
    },
}

# Override native layouts while keeping the same canonical signal semantics.
# This raw array mixes quantities; only the selected setpoint maximum is in A.
# The metadata describes extraction for consumers; the generator reads no ADOs.
ADO_SIGNAL_SPEC_OVERRIDES = {
    "Bend": {
        "current_range": {
            "native_description": (
                "Main-dipole maxima for [setpoint, status, reference, B field, "
                "DC Current Transformer, error]. Allowed current range is "
                "[0, value[0]] A (zero-based array index)."
            ),
            "native_unit": "none",
            "MetaP": {"additional_metadata": [
                {"key": "array_order", "value": "setpoint,status,reference,B field,DC Current Transformer,error", "datatype": "String"},
                {"key": "array_length", "value": "6", "datatype": "Integer"},
                {"key": "array_value_semantics", "value": "maximum", "datatype": "String"},
                {"key": "current_range_maximum_index", "value": "0", "datatype": "Integer"},
                {"key": "array_index_base", "value": "0", "datatype": "Integer"},
                {"key": "current_range_minimum", "value": "0", "datatype": "Float"},
                {"key": "current_range_unit", "value": "A", "datatype": "String"},
                {"key": "current_range_order", "value": "minimum,maximum", "datatype": "String"},
            ]},
        },
    },
}


# The shared bmm range has the same native layout for dipoles and quadrupoles.
ADO_SIGNAL_SPEC_OVERRIDES["Quadrupole"] = {
    "main_current_range": ADO_SIGNAL_SPEC_OVERRIDES["Bend"]["current_range"],
}


ADO_SIGNAL_DEFAULTS = {
    "kind": "Signal",
    "source_system": "Other",
    "access_protocol": "ADO",
}

BOOSTER_DOCUMENT_ENRICHMENT = {
    "facility_identifiers": [
        {"identifier_type": "LOCAL", "identifier_value": "BOOSTER"},
    ],
    "description": "NARAD representation of the Booster beamline enriched with ADO controls.",
    "notes": [
        "Enriched with Booster BPM, corrector, quadrupole, sextupole, and main-dipole ADO signal naming rules.",
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


def normalize_parameter_groups(entity: dict[str, Any]) -> None:
    for group_name, group in entity.items():
        if group_name.endswith("P") and isinstance(group, dict):
            group.setdefault("id", f"{entity['id']}/{group_name}")
            if isinstance(group.get("alias"), str):
                group["alias"] = [group["alias"]]


def device_name(component: dict[str, Any]) -> str:
    """Strip only the occurrence suffix added during lattice expansion."""
    return re.sub(r"_\d{3}$", "", local_name(component["id"]))


def apply_booster_kind_rules(components: list[dict[str, Any]]) -> None:
    """Specialize PALS device kinds using the first matching Booster kind rule."""
    for component in components:
        name = device_name(component)
        for rule in BOOSTER_KIND_RULES:
            name_pattern = rule.get("name_pattern")
            matches = name in rule.get("names", ()) or (
                name_pattern is not None
                and re.fullmatch(name_pattern, name, flags=re.IGNORECASE) is not None
            )
            if not matches:
                continue
            if component["kind"] not in {rule["source_kind"], rule["target_kind"]}:
                raise ValueError(
                    f"Booster kind rule for {name} expects {rule['source_kind']} or "
                    f"{rule['target_kind']}, found {component['kind']}"
                )
            component["kind"] = rule["target_kind"]
            component["functions"] = default_functions(rule["target_kind"])
            break


def resolve_ado_name(
    name: str, rules: list[tuple[str, tuple[AdoTemplate, AdoTemplate]]]
) -> str | None:
    """Resolve the first full-name match using canonical uppercase element names."""
    for pattern, (device_template, attribute_template) in rules:
        match = re.fullmatch(pattern, name.upper(), flags=re.IGNORECASE)
        if match:
            device = (
                device_template(match) if callable(device_template)
                else match.expand(device_template)
            )
            attribute = (
                attribute_template(match) if callable(attribute_template)
                else match.expand(attribute_template)
            )
            return f"{device}:{attribute}"
    return None


def resolve_ado_names(component: dict[str, Any]) -> dict[str, str]:
    """Resolve signal mappings from ADO_RULES for any configured component kind."""
    names = {}
    for semantic_name, rules in ADO_RULES.get(component["kind"], {}).items():
        ado_name = resolve_ado_name(device_name(component), rules)
        if ado_name is not None:
            names[semantic_name] = ado_name
    return names


def generate_ado_signals(
    components: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Generate deduplicated ADO signals and component bindings."""
    signals_by_id: dict[str, dict[str, Any]] = {}
    bindings: list[dict[str, Any]] = []

    for component in components:
        for semantic_name, ado_name in resolve_ado_names(component).items():
            spec = {
                **ADO_SIGNAL_SPECS[semantic_name.removeprefix("stopband_").removeprefix("main_").removeprefix("backleg_")],
                **ADO_SIGNAL_SPEC_OVERRIDES.get(component["kind"], {}).get(semantic_name, {}),
            }
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
                "alias": [semantic_name.removeprefix("main_")],
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


def add_polarity_metadata(components: list[dict[str, Any]]) -> None:
    """Apply supply-scoped polarity metadata from the configured rules."""
    for component in components:
        for rule in POLARITY_RULES.values():
            if component["kind"] != rule["kind"] or not re.fullmatch(
                rule["name_pattern"], device_name(component), flags=re.IGNORECASE
            ):
                continue
            if rule["polarity"] not in (-1, 1):
                raise ValueError("Supply polarity must be -1 or +1")
            role = rule["role"]
            values = {
                f"{role}_supply": (rule["supply"], "String"),
                f"{role}_current_polarity": (str(rule["polarity"]), "Integer"),
                **{key: (value, "String") for key, value in rule.get("metadata", {}).items()},
            }
            entries = component.setdefault("MetaP", {}).setdefault("additional_metadata", [])
            entries[:] = [entry for entry in entries if entry["key"] not in values]
            entries.extend(
                {"key": key, "value": value, "datatype": datatype}
                for key, (value, datatype) in values.items()
            )
            normalize_parameter_groups(component)


def enrich_document(skeleton: dict[str, Any]) -> dict[str, Any]:
    """Return a Booster-enriched copy of a signal-free NARAD skeleton."""
    document = deepcopy(skeleton)
    facility = document["facility"]
    if facility.get("signals") or facility.get("signal_bindings"):
        raise ValueError("expected a skeleton with empty signals and signal_bindings")

    apply_booster_kind_rules(facility["components"])
    add_polarity_metadata(facility["components"])
    signals, bindings = generate_ado_signals(facility["components"])
    facility["signals"] = signals
    facility["signal_bindings"] = bindings
    facility.setdefault("identifiers", []).extend(
        deepcopy(BOOSTER_DOCUMENT_ENRICHMENT["facility_identifiers"])
    )
    document["description"] = BOOSTER_DOCUMENT_ENRICHMENT["description"]
    document.setdefault("notes", []).extend(BOOSTER_DOCUMENT_ENRICHMENT["notes"])
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
