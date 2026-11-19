#!/usr/bin/env python3
"""Translate a PALS YAML lattice to a control-system-neutral NARAD skeleton.

Usage: python pals_to_narad.py -input INPUT_PALS_YAML -output OUTPUT_SKELETON_YAML
Run ``python pals_to_narad.py -help`` for option details.

Unsupported expanded element kinds are listed in a warning and omitted without
creating a precedence relation across the resulting gap; users must decide how
those kinds should map to NARAD. Multipass is derived from the source beamline,
but NARAD does not yet define multipass identity and relationships.

This translator uses ``src/narad/datamodel/narad_pydantic.py`` for NARAD class
discovery and validation. Run ``just gen-python`` after changing ``narad.yaml``
so the generated models remain synchronized with the schema.
"""

from __future__ import annotations

import argparse
from datetime import date
import warnings
from collections import Counter
from copy import deepcopy
from pathlib import Path
import re
from typing import Any

from pydantic import BaseModel, ValidationError
import yaml

from narad.datamodel import narad_pydantic as narad_model
from translators.yaml_order import order_document_components


class PalsYamlLoader(yaml.SafeLoader):
    """Safe YAML loader that recognizes plain scientific-notation floats."""


PalsYamlLoader.add_implicit_resolver(
    "tag:yaml.org,2002:float",
    re.compile(r"^[+-]?[0-9][0-9_]*(?:\.[0-9_]*)?[eE][+-]?[0-9]+$"),
    list("-+0123456789"),
)

# Translation semantics belong to the PALS-to-NARAD boundary rather than the
# general NARAD schema. Subclasses inherit the nearest rule through their MRO.
DEFAULT_FUNCTION_BY_KIND = {
    "BeamLine": "BeamLineSection",
    "Solenoid": "Focusing",
    "Multipole": "Focusing",
    "Bend": "Steering",
    "Kicker": "Steering",
    "DiagnosticDevice": "Measurement",
    "BeamProfileMonitor": "BeamProfileMeasurement",
    "BeamPositionMonitor": "BeamPositionMeasurement",
    "RadiationMonitor": "RadiationMonitoring",
    "CrabCavity": "Steering",
    "RFCavity": "BeamAcceleration",
    "SupportingFacilityComponent": "Support",
    "BookkeepingComponent": "Mark",
    "Drift": "DriftSpace",
    "BeamLineSection": "BeamLineSection",
}

def parameter_groups(model: type[BaseModel]) -> tuple[str, ...]:
    """Derive the parameter groups accepted by a NARAD component class."""
    return tuple(name for name in model.model_fields if name.endswith("P"))


def component_functions(model: type[BaseModel]) -> list[str] | None:
    """Return the nearest translator-owned default function in the hierarchy."""
    for ancestor in model.__mro__:
        function = DEFAULT_FUNCTION_BY_KIND.get(ancestor.__name__)
        if function is not None:
            return [function]
    return None


def translatable_component_models() -> list[type[BaseModel]]:
    """Return generated component models with PALS translation semantics."""
    models: list[type[BaseModel]] = []
    for candidate in vars(narad_model).values():
        if not isinstance(candidate, type) or not issubclass(
            candidate, narad_model.Component
        ):
            continue
        if component_functions(candidate) is None:
            continue
        if candidate not in models:
            models.append(candidate)
    return models


def general_mapping_candidate(
    candidates: list[type[BaseModel]],
) -> type[BaseModel] | None:
    """Return the unique candidate that is a superclass of all candidates."""
    general = [
        candidate
        for candidate in candidates
        if all(issubclass(other, candidate) for other in candidates)
    ]
    return general[0] if len(general) == 1 else None


def component_model(source_kind: str) -> type[BaseModel] | None:
    """Resolve a PALS kind using NARAD names and schema mapping metadata."""
    models = translatable_component_models()
    same_name = getattr(narad_model, source_kind, None)
    if same_name in models:
        return same_name

    mapping = f"pals:{source_kind}"
    for mapping_type in ("exact_mappings", "broad_mappings"):
        candidates = [
            model
            for model in models
            if mapping in dict(model.linkml_meta).get(mapping_type, [])
        ]
        if len(candidates) == 1:
            return candidates[0]
        if candidates:
            return general_mapping_candidate(candidates)
    return None


def translation_rule(source_kind: str) -> dict[str, Any] | None:
    """Derive structural mapping from NARAD and add translation semantics."""
    model = component_model(source_kind)
    if model is None:
        return None
    functions = component_functions(model)
    if functions is None:
        return None
    groups = parameter_groups(model)
    return {
        "target_kind": model.__name__,
        "model": model,
        "functions": functions,
        "parameter_groups": groups,
        "has_length": "LongitudinalPlacementP" in groups,
        "plane_from_bmad": issubclass(model, narad_model.Kicker),
    }


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
    """Convert flattened PALS multipole fields to mag_components by order."""
    components: dict[int, dict[str, Any]] = {}
    for key, value in group.items():
        match = re.fullmatch(r"(tilt|Kn|Ks|Bn|Bs)(\d+)(L?)", key)
        if not match:
            continue
        field, order_text, integrated = match.groups()
        if field == "tilt" and integrated:
            continue
        order = int(order_text)
        output_field = f"{field}L" if integrated else field
        components.setdefault(order, {"order": order})[output_field] = value
    if not components:
        return None
    for order, component in components.items():
        representations = {
            field[0] + ("L" if field.endswith("L") else "")
            for field in component
            if field not in {"order", "tilt"}
        }
        if len(representations) > 1:
            fields = ", ".join(
                field for field in component if field not in {"order", "tilt"}
            )
            raise ValueError(
                f"multipole order {order} mixes incompatible strength types: {fields}"
            )
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
    rule = translation_rule(str(source_kind))
    if rule is None:
        return None

    component: dict[str, Any] = {
        "id": instance_id(name),
        "kind": rule["target_kind"],
        "native_types": native_types(source),
        "functions": list(rule["functions"]),
        "beamline_relation": "Inline",
    }

    if rule["has_length"]:
        component["LongitudinalPlacementP"] = {
            "length": float(source.get("length", 0.0))
        }

    for group_name in rule["parameter_groups"]:
        source_group = source.get(group_name)
        if not source_group:
            continue
        if group_name == "MagneticMultipoleP":
            source_group = magnetic_multipoles(source_group)
        if source_group:
            component[group_name] = deepcopy(source_group)

    if rule.get("plane_from_bmad"):
        bmad_key = source.get("Bmad", {}).get("Bmad_key", "")
        if bmad_key == "HKicker":
            component["plane"] = "Horizontal"
        elif bmad_key == "VKicker":
            component["plane"] = "Vertical"

    normalize_parameter_groups(component)
    validated = rule["model"].model_validate(component)
    return validated.model_dump(mode="json", exclude_none=True)


def mapped_elements(
    expanded_line: list[tuple[str, dict[str, Any]]],
) -> list[tuple[str, dict[str, Any] | None]]:
    """Map an expanded line while retaining gaps for unsupported elements."""
    mapped: list[tuple[str, dict[str, Any] | None]] = []
    unsupported: Counter[tuple[str, str]] = Counter()
    for name, source in expanded_line:
        try:
            component = component_from_pals(name, source)
        except (ValueError, ValidationError) as exc:
            warnings.warn(
                f"Invalid PALS element {name!r} was omitted: {exc}",
                UserWarning,
                stacklevel=2,
            )
            component = None
        mapped.append((name, component))
        if component is None:
            unsupported[(name, str(source.get("kind", "<missing kind>")))] += 1

    if unsupported:
        details = ", ".join(
            f"{name} ({kind})" + (f" x{count}" if count > 1 else "")
            for (name, kind), count in sorted(unsupported.items())
        )
        warnings.warn(
            "Unsupported or invalid PALS elements were omitted from the NARAD skeleton: "
            f"{details}. No precedence relation was created across an omitted "
            "element. Decide how these PALS kinds should map to NARAD before "
            "using the skeleton as a complete lattice.",
            UserWarning,
            stacklevel=2,
        )
    return mapped


def load_pals(
    path: Path,
) -> tuple[
    dict[str, Any],
    dict[str, dict[str, Any]],
    list[tuple[str, dict[str, Any], dict[str, Any]]],
]:
    """Load records and select the beamline branches of the active lattice."""
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

    selected_names = [
        str(record["use"])
        for record in records
        if isinstance(record, dict) and record.get("use") is not None
    ]
    if len(selected_names) > 1:
        raise ValueError(
            "expected at most one PALS use statement; "
            f"found {len(selected_names)}"
        )
    if selected_names:
        lattice_name = selected_names[0]
    else:
        lattice_names = [
            name for name, value in named.items() if value.get("kind") == "Lattice"
        ]
        if len(lattice_names) != 1:
            raise ValueError(
                "expected one selected PALS lattice or exactly one Lattice record; "
                f"found {len(lattice_names)} lattice records"
            )
        lattice_name = lattice_names[0]

    lattice = resolve_record(lattice_name, {}, named)
    if lattice.get("kind") != "Lattice":
        raise ValueError(f"PALS use target {lattice_name!r} is not a Lattice")
    branch_items = lattice.get("branches", [])
    if not isinstance(branch_items, list) or not branch_items:
        raise ValueError(f"Lattice {lattice_name!r} has no branches")

    branches: list[tuple[str, dict[str, Any], dict[str, Any]]] = []
    for item in branch_items:
        branch_name, branch_override = parse_line_item(item)
        branch = resolve_record(branch_name, branch_override, named)
        if branch.get("kind") != "BeamLine":
            raise ValueError(
                f"Lattice branch {branch_name!r} is not a BeamLine"
            )
        branches.append((branch_name, branch_override, branch))
    return pals, named, branches


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


def beamline_is_multipass(
    name: str,
    override: dict[str, Any],
    records: dict[str, dict[str, Any]],
    expansion_stack: tuple[str, ...] = (),
) -> bool:
    """Return whether a beamline or any nested beamline is multipass."""
    if name in expansion_stack:
        cycle = " -> ".join((*expansion_stack, name))
        raise ValueError(f"cyclic BeamLine reference: {cycle}")

    beamline = resolve_record(name, override, records)
    if bool(beamline.get("multipass", False)):
        return True

    for item in beamline.get("line", []):
        item_name, item_override = parse_line_item(item)
        resolved = resolve_record(item_name, item_override, records)
        if int(resolved.get("repeat", 1)) == 0:
            continue
        if resolved.get("kind") == "BeamLine" and beamline_is_multipass(
            item_name,
            item_override,
            records,
            (*expansion_stack, name),
        ):
            return True
    return False


def warn_multipass(beamline_name: str) -> None:
    """Report the current NARAD modeling limitation for a multipass beamline."""
    warnings.warn(
        f"Beamline {beamline_name!r} is multipass, but multipass identity and "
        "relationships are not yet defined in NARAD schema. The generated components "
        "and precedence relations may not represent shared physical elements "
        "across passes correctly.",
        UserWarning,
        stacklevel=2,
    )


def build_document(source_path: Path) -> dict[str, Any]:
    """Build a signal-free NARAD skeleton from a PALS export."""
    pals, records, source_beamlines = load_pals(source_path)
    named_components = {
        name: component
        for name, source in records.items()
        if source.get("kind") not in {"BeamLine", "Lattice"}
        if (component := component_from_pals(name, source)) is not None
    }

    components: list[dict[str, Any]] = []
    component_ids: set[str] = set()
    used_names: set[str] = set()
    relations: list[dict[str, Any]] = []
    beamlines: list[dict[str, Any]] = []

    for beamline_name, beamline_override, beamline in source_beamlines:
        multipass = beamline_is_multipass(beamline_name, beamline_override, records)
        if multipass:
            warn_multipass(beamline_name)
        expanded_line = expand_beamline(beamline_name, beamline_override, records)
        mapped_line = mapped_elements(expanded_line)
        occurrence_totals = Counter(
            name for name, component in mapped_line if component is not None
        )
        occurrence_numbers: Counter[str] = Counter()
        ordered_ids: list[str | None] = []
        for name, source_component in mapped_line:
            if source_component is None:
                ordered_ids.append(None)
                continue
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
                "predicate": "Precedes",
                "object": obj,
                "context": "beamline_order",
                "beamline_context": beamline_id,
            }
            for subject, obj in zip(ordered_ids, ordered_ids[1:])
            if subject is not None and obj is not None
        )
        beamlines.append(
            {
                "id": beamline_id,
                "kind": "BeamLine",
                "functions": component_functions(narad_model.BeamLine),
                "beamline_relation": "Inline",
                "multipass": multipass,
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

    document = {
        "description": f"Control-system-neutral NARAD skeleton generated from {source_path.name}.",
        "kind": "PALSAccelerator",
        "version": "0.1.0",
        "created_date": date.today().isoformat(),
        "change_log": [
            {
                "change_date": date.today().isoformat(),
                "instance_version": "0.1.0",
                "summary": "Initial PALS-to-NARAD translation.",
            }
        ],
        "notes": notes,
        "facility": {
            "components": components,
            "beamlines": beamlines,
            "signals": [],
            "signal_bindings": [],
            "component_relations": relations,
        },
    }
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
        help="NARAD skeleton YAML file to create under .local/translation/skeletons by default.",
    )

    args = parser.parse_args()

    # Try to derive default output name from input name
    if args.output is None:
        input_name = args.input.name  # e.g. "fodo.pals.yaml"
        parts = input_name.split(".")

        # Expect format: "filename.pals.yaml" → exactly 3 parts with middle part "pals"
        if len(parts) == 3 and parts[1] == "pals" and parts[2] == "yaml":
            repo_root = Path(__file__).resolve().parents[2]
            args.output = (
                repo_root
                / ".local"
                / "translation"
                / "skeletons"
                / f"{parts[0]}_narad_skeleton.yaml"
            )
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
