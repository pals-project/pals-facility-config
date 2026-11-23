"""Lifecycle metadata owned by final NARAD instance generators."""

from __future__ import annotations

from copy import deepcopy
from datetime import date
from typing import Any


LIFECYCLE_FIELDS = ("version", "created_date", "updated_date", "change_log")


def initialize_final_instance(
    document: dict[str, Any],
    *,
    summary: str,
    creation_date: date | None = None,
    existing_document: dict[str, Any] | None = None,
) -> None:
    """Preserve an existing lifecycle or initialize it for a new final instance."""
    for field in LIFECYCLE_FIELDS:
        document.pop(field, None)

    if existing_document is not None:
        existing_lifecycle = {
            field: deepcopy(existing_document[field])
            for field in LIFECYCLE_FIELDS
            if field in existing_document
        }
        if "created_date" in existing_lifecycle and "change_log" in existing_lifecycle:
            document.update(existing_lifecycle)
            return

    created = (creation_date or date.today()).isoformat()
    document["version"] = "0.0.0"
    document["created_date"] = created
    document["change_log"] = [
        {
            "change_date": created,
            "instance_version": "0.0.0",
            "summary": summary,
        }
    ]
