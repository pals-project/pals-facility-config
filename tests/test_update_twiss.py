"""Regression coverage for the shared Twiss table importer."""

import importlib.util
from pathlib import Path
import sys

import pytest
import yaml


BOOSTER = Path(__file__).resolve().parents[1] / "examples" / "Booster"
spec = importlib.util.spec_from_file_location("update_twiss", BOOSTER.parent / "update_twiss.py")
updater = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = updater
spec.loader.exec_module(updater)


def test_reordered_partial_columns_and_extra_columns(tmp_path):
    table = tmp_path / "twiss.dat"
    table.write_text(
        "# Downstream optics\n"
        "# beta_b name orbit_x s dbeta_a_dpz beta_a\n"
        "--- BEGINNING ignored 0.0 2.3D+01 6.0\n"
        "Lord Elements:\n"
        "ignored trailing table\n"
    )
    rows = updater.read_twiss_table(table)
    assert rows == [updater.TwissRow("BEGINNING", 0.0, {"dbeta_a_dpz": 23.0, "beta_a": 6.0})]


def test_merge_preserves_existing_fields_and_group_id():
    document = {
        "kind": "PALSAccelerator",
        "facility": {"components": [{
            "id": "inst:BEGINNING_B1",
            "kind": "BeginningEle",
            "functions": ["Mark"],
            "beamline_relation": "Inline",
            "TwissP": {
                "id": "inst:custom_twiss",
                "beta_a": 5.0,
                "dbeta_a_dpz": 23.85,
            },
        }]},
    }
    assert updater.add_twiss_data(
        document, [updater.TwissRow("BEGINNING", 0.0, {"beta_a": 6.0})]
    ) == (0, 1)
    assert document["facility"]["components"][0]["TwissP"] == {
        "id": "inst:custom_twiss", "beta_a": 6.0, "dbeta_a_dpz": 23.85,
    }


@pytest.mark.parametrize("text, message", [
    ("0 BEGINNING 0.0 6.0\n", "expected a header"),
    ("# name s beta_a\nBEGINNING 0.0\n", "expected 3 columns"),
    ("# name s beta_a\nBEGINNING 0.0 bad\n", "invalid numeric"),
    ("# name s beta_a beta_a\n", "duplicate column"),
])
def test_malformed_tables_are_rejected(tmp_path, text, message):
    table = tmp_path / "twiss.dat"
    table.write_text(text)
    with pytest.raises(ValueError, match=message):
        updater.read_twiss_table(table)


def test_booster_table_preserves_beginning_optics():
    document = yaml.safe_load((BOOSTER / "booster_narad_skeleton_palsparserpy.yaml").read_text())
    beginning = document["facility"]["components"][0]
    original = dict(beginning["TwissP"])
    rows = updater.read_twiss_table(BOOSTER / "booster_twiss.dat")
    updater.add_twiss_data(document, rows)
    for name, value in original.items():
        if name not in rows[0].twiss:
            assert beginning["TwissP"][name] == value
    assert beginning["TwissP"]["beta_a"] == rows[0].twiss["beta_a"]


def test_partial_overlap_repeated_names_and_missing_values(tmp_path):
    table = tmp_path / "twiss.dat"
    table.write_text(
        "# name s beta_a beta_b\n"
        "removed 1.0 99.0 99.0\n"
        "mark 2.0 6.0 ---\n"
        "MARK 3.0 7.0 8.0\n"
        "mark 4.0 99.0 99.0\n"
    )
    document = {
        "kind": "PALSAccelerator",
        "facility": {"components": [
            {"id": "inst:MARK", "kind": "Marker",
             "TwissP": {"id": "inst:first", "beta_b": 10.0, "dbeta_a_dpz": 23.0}},
            {"id": "inst:MARK_002", "kind": "Marker"},
            {"id": "inst:OTHER", "kind": "Marker",
             "TwissP": {"id": "inst:other", "beta_a": 11.0}},
        ]},
    }
    for component in document["facility"]["components"]:
        component.update(functions=["Mark"], beamline_relation="Inline")
    assert updater.add_twiss_data(document, updater.read_twiss_table(table)) == (0, 2)
    first, second, other = document["facility"]["components"]
    assert first["TwissP"] == {
        "id": "inst:first", "beta_a": 6.0, "beta_b": 10.0, "dbeta_a_dpz": 23.0,
    }
    assert second["TwissP"] == {
        "id": "inst:MARK_002/TwissP", "beta_a": 7.0, "beta_b": 8.0,
    }
    assert other["TwissP"] == {"id": "inst:other", "beta_a": 11.0}
