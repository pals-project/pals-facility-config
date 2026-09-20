#!/usr/bin/env python3
"""Translate a PALS lattice to a control-neutral NARAD skeleton with PALSParserPy.

Usage: python palsparserpy_to_narad.py -input INPUT_PALS_YAML [-output OUTPUT_YAML]
Run ``python palsparserpy_to_narad.py -help`` for option details.

PALSParserPy and its compiled PALSParserCpp library must be available in the
active Python environment.  PALSParserPy owns PALS parsing, inheritance, nested
beamline expansion, and signed repeats; this module owns the NARAD mapping.
Unsupported expanded element kinds are listed in a warning and omitted without
creating a precedence relation across the resulting gap; users must decide how
those kinds should map to NARAD. Multipass is derived from PALS expansion data,
but NARAD does not yet define multipass identity and relationships.

This translator uses ``src/narad/datamodel/narad_pydantic.py`` for NARAD class
discovery and validation. Run ``just gen-python`` after changing ``narad.yaml``
so the generated models remain synchronized with the schema.
"""

from __future__ import annotations

import argparse
import re
import warnings
from collections import Counter
from copy import deepcopy
from pathlib import Path
from typing import Any

import palsparserpy as pp
from pydantic import BaseModel, ValidationError
import yaml

from narad.datamodel import narad_pydantic as narad_model


class PalsYamlLoader(yaml.SafeLoader):
    """Safe YAML loader that recognizes plain scientific-notation floats."""


PalsYamlLoader.add_implicit_resolver(
    "tag:yaml.org,2002:float",
    re.compile(r"^[+-]?[0-9][0-9_]*(?:\.[0-9_]*)?[eE][+-]?[0-9]+$"),
    list("-+0123456789"),
)


def parameter_groups(model: type[BaseModel]) -> tuple[str, ...]:
    """Derive the parameter groups accepted by a NARAD component class."""
    return tuple(name for name in model.model_fields if name.endswith("P"))


def component_functions(model: type[BaseModel]) -> list[str] | None:
    """Read the nearest default_function annotation in the model hierarchy."""
    for ancestor in model.__mro__:
        metadata = ancestor.__dict__.get("linkml_meta")
        if metadata is None:
            continue
        annotation = dict(metadata).get("annotations", {}).get("default_function")
        if annotation is not None:
            value = annotation.get("value") if isinstance(annotation, dict) else annotation
            return [str(value)]
    return None


def concrete_component_models() -> list[type[BaseModel]]:
    """Return concrete generated Pydantic models for NARAD components."""
    models: list[type[BaseModel]] = []
    for candidate in vars(narad_model).values():
        if not isinstance(candidate, type) or not issubclass(
            candidate, narad_model.Component
        ):
            continue
        if dict(candidate.linkml_meta).get("abstract", False):
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
    models = concrete_component_models()
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


def node_as_python(node: Any) -> Any:
    """Convert a PALSParserPy YAMLNode tree to ordinary Python values."""
    return yaml.load(pp.to_yaml_string(node), Loader=PalsYamlLoader)


def selected_branch(lattices: Any) -> tuple[str, dict[str, Any]]:
    """Return the selected lattice's only branch.

    How multiple PALS branches should map to NARAD instances is still a schema
    design decision, so this experimental translator rejects that case clearly.
    """
    expanded = node_as_python(lattices.expanded)
    if not isinstance(expanded, dict) or len(expanded) != 1:
        count = len(expanded) if isinstance(expanded, dict) else 0
        raise ValueError(
            "expected PALSParserPy to select exactly one lattice; "
            f"found {count}"
        )

    _, lattice = next(iter(expanded.items()))
    branches = lattice.get("branches", [])
    if not isinstance(branches, list) or len(branches) != 1:
        count = len(branches) if isinstance(branches, list) else 0
        raise ValueError(
            "this translator currently supports exactly one branch per PALS "
            f"lattice; found {count}"
        )

    branch_entry = branches[0]
    if not isinstance(branch_entry, dict) or len(branch_entry) != 1:
        raise ValueError("expected each PALS branch to be a single-name mapping")
    branch_name, branch = next(iter(branch_entry.items()))
    if not isinstance(branch, dict) or not isinstance(branch.get("line"), list):
        raise ValueError(f"expected branch {branch_name!r} to contain a line list")
    return str(branch_name), branch


def mapped_elements(
    branch: dict[str, Any],
) -> list[tuple[str, dict[str, Any] | None]]:
    """Map an expanded line while retaining gaps for unsupported elements."""
    mapped: list[tuple[str, dict[str, Any] | None]] = []
    unsupported: Counter[tuple[str, str]] = Counter()
    for entry in branch["line"]:
        if isinstance(entry, str):
            mapped.append((entry, None))
            unsupported[(entry, "unresolved reference")] += 1
            continue
        if not isinstance(entry, dict) or len(entry) != 1:
            raise ValueError(f"invalid expanded PALS line entry: {entry!r}")
        name, source = next(iter(entry.items()))
        if not isinstance(source, dict):
            mapped.append((str(name), None))
            unsupported[(str(name), "missing property mapping")] += 1
            continue
        try:
            component = component_from_pals(str(name), source)
        except (ValueError, ValidationError) as exc:
            warnings.warn(
                f"Invalid PALS element {name!r} was omitted: {exc}",
                UserWarning,
                stacklevel=2,
            )
            component = None
        mapped.append((str(name), component))
        if component is None:
            unsupported[(str(name), str(source.get("kind", "<missing kind>")))] += 1

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


def is_multipass(branch: dict[str, Any]) -> bool:
    """Return whether the branch or any expanded sub-line is multipass."""
    if bool(branch.get("multipass", False)):
        return True
    return any(
        isinstance(entry, dict)
        and any(
            isinstance(source, dict) and "multipass_index" in source
            for source in entry.values()
        )
        for entry in branch["line"]
    )


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


def source_notes(lattices: Any) -> list[str]:
    """Read top-level PALS notes from the combined, pre-expansion tree."""
    combined = node_as_python(lattices.combined)
    notes = combined.get("PALS", {}).get("notes", []) if isinstance(combined, dict) else []
    if notes is None:
        return []
    if isinstance(notes, list):
        return [str(note) for note in notes]
    return [str(notes)]


def build_document(source_path: Path) -> dict[str, Any]:
    """Build a signal-free NARAD skeleton from a PALSParserPy expansion."""
    lattices = pp.parse_and_expand_pals(source_path.resolve(), problems="none")
    for problem in lattices.problems:
        warnings.warn(str(problem), UserWarning, stacklevel=2)

    beamline_name, branch = selected_branch(lattices)
    multipass = is_multipass(branch)
    if multipass:
        warn_multipass(beamline_name)
    mapped_line = mapped_elements(branch)
    occurrence_totals = Counter(
        name for name, component in mapped_line if component is not None
    )
    occurrence_numbers: Counter[str] = Counter()

    components: list[dict[str, Any]] = []
    ordered_ids: list[str | None] = []
    for name, source_component in mapped_line:
        if source_component is None:
            ordered_ids.append(None)
            continue
        component = deepcopy(source_component)
        if occurrence_totals[name] > 1:
            occurrence_numbers[name] += 1
            component["id"] = instance_id(f"{name}_{occurrence_numbers[name]:03d}")
            normalize_parameter_groups(component, replace_ids=True)
        components.append(component)
        ordered_ids.append(component["id"])

    beamline_id = instance_id(beamline_name)
    relations = [
        {
            "id": f"inst:{beamline_name.upper()}_{subject[5:]}_PRECEDES_{obj[5:]}",
            "subject": subject,
            "predicate": "pals:precedes",
            "object": obj,
            "context": "beamline_order",
            "beamline_context": beamline_id,
        }
        for subject, obj in zip(ordered_ids, ordered_ids[1:])
        if subject is not None and obj is not None
    ]

    notes = source_notes(lattices)
    notes.append(
        "Generated from a PALSParserPy-expanded lattice without control system "
        "enrichment."
    )

    document = {
        "description": (
            "Control-system-neutral NARAD skeleton generated from "
            f"{source_path.name} using PALSParserPy."
        ),
        "kind": "PALSAccelerator",
        "version": "0.1.0",
        "notes": notes,
        "facility": {
            "components": components,
            "beamlines": [
                {
                    "id": beamline_id,
                    "kind": "BeamLine",
                    "functions": component_functions(narad_model.BeamLine),
                    "beamline_relation": "Inline",
                    "multipass": multipass,
                    "periodic": bool(branch.get("periodic", False)),
                    "description": (
                        f"Beamline imported from PALSParserPy branch {beamline_name}."
                    ),
                }
            ],
            "signals": [],
            "signal_bindings": [],
            "component_relations": relations,
        },
    }
    validated = narad_model.PALSAccelerator.model_validate(document)
    return validated.model_dump(mode="json", exclude_none=True)


def default_output_path(input_path: Path) -> Path:
    """Derive a filename that distinguishes PALSParserPy-generated skeletons."""
    suffix = ".pals.yaml"
    if not input_path.name.endswith(suffix):
        raise ValueError(
            f"cannot derive output name from {input_path.name!r}; "
            "provide -output explicitly"
        )
    stem = input_path.name[: -len(suffix)]
    return input_path.parent / f"{stem}_narad_skeleton_palsparserpy.yaml"


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
        help="PALS YAML file to parse and translate",
    )
    parser.add_argument(
        "-output",
        "--output",
        type=Path,
        metavar="OUTPUT_SKELETON_YAML",
        help=(
            "NARAD skeleton to create; defaults to "
            "'filename_narad_skeleton_palsparserpy.yaml'"
        ),
    )
    args = parser.parse_args()
    if args.output is None:
        try:
            args.output = default_output_path(args.input)
        except ValueError as exc:
            parser.error(str(exc))
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
