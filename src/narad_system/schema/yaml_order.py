"""Stable, human-friendly field ordering for serialized NARAD YAML."""

from __future__ import annotations

from typing import Any


COMPONENT_HEADER_FIELDS = (
    "id",
    "kind",
    "native_types",
    "functions",
    "beamline_relation",
)


def order_component_fields(component: dict[str, Any]) -> dict[str, Any]:
    """Put identity fields first and inlined PALS parameter groups last."""
    ordered: dict[str, Any] = {}
    for field in COMPONENT_HEADER_FIELDS:
        if field in component:
            ordered[field] = component[field]
    for field, value in component.items():
        if field not in ordered and not field.endswith("P"):
            ordered[field] = value
    for field, value in component.items():
        if field not in ordered:
            ordered[field] = value
    return ordered


def order_document_components(document: dict[str, Any]) -> dict[str, Any]:
    """Apply the canonical display order to every component in a document."""
    facility = document.get("facility")
    if not isinstance(facility, dict):
        return document
    components = facility.get("components")
    if isinstance(components, list):
        facility["components"] = [
            order_component_fields(component)
            if isinstance(component, dict)
            else component
            for component in components
        ]
    return document
