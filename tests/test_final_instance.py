"""Final-instance lifecycle metadata regressions."""

from datetime import date
from pathlib import Path

import pytest
import yaml

from translators.final_instance import initialize_final_instance


EXAMPLES = Path(__file__).resolve().parents[1] / "examples"


def test_final_generator_replaces_skeleton_lifecycle_placeholders():
    document = {
        "version": "9.9.9",
        "created_date": "2000-01-01",
        "updated_date": "2000-01-02",
        "change_log": [{"summary": "Skeleton placeholder."}],
    }

    initialize_final_instance(
        document,
        summary="Initial final instance creation.",
        creation_date=date(2026, 11, 20),
    )

    assert document == {
        "version": "0.0.0",
        "created_date": "2026-11-20",
        "change_log": [
            {
                "change_date": "2026-11-20",
                "instance_version": "0.0.0",
                "summary": "Initial final instance creation.",
            }
        ],
    }


def test_final_generator_preserves_existing_creation_history():
    existing = {
        "version": "0.0.1",
        "created_date": "2026-11-19",
        "updated_date": "2026-11-20",
        "change_log": [{"summary": "Existing history."}],
    }
    document = {"version": "9.9.9", "created_date": "2000-01-01"}

    initialize_final_instance(
        document,
        summary="Ignored for an existing instance.",
        creation_date=date(2030, 1, 1),
        existing_document=existing,
    )

    assert document == existing


@pytest.mark.parametrize(
    ("filename", "created_date"),
    [
        ("bta_narad_instance.yaml", "2026-10-09"),
        ("booster_narad_instance.yaml", "2026-10-29"),
        ("toy_ring_narad_instance.yaml", "2026-11-06"),
    ],
)
def test_tracked_instance_history(filename: str, created_date: str):
    document = yaml.safe_load((EXAMPLES / filename).read_text(encoding="utf-8"))

    assert document["version"] == "0.0.1"
    assert document["created_date"] == created_date
    assert document["updated_date"] == "2026-11-19"
    assert [entry["instance_version"] for entry in document["change_log"]] == [
        "0.0.0",
        "0.0.1",
    ]
    assert [entry["change_date"] for entry in document["change_log"]] == [
        created_date,
        "2026-11-19",
    ]


@pytest.mark.parametrize(
    "filename", ["bta_narad_instance.yaml", "booster_narad_instance.yaml"]
)
def test_real_bnl_instances_have_affiliation(filename: str):
    document = yaml.safe_load((EXAMPLES / filename).read_text(encoding="utf-8"))

    assert document["affiliation"] == {
        "id": "brookhaven-national-laboratory",
        "name": "Brookhaven National Laboratory",
        "identifiers": [
            {
                "identifier_type": "ROR",
                "identifier_value": "https://ror.org/02ex6cf31",
            }
        ],
    }


def test_fictional_toy_ring_has_no_affiliation():
    document = yaml.safe_load(
        (EXAMPLES / "toy_ring_narad_instance.yaml").read_text(encoding="utf-8")
    )
    assert "affiliation" not in document
