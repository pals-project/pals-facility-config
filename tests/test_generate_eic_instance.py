"""EIC toy-ring EPICS enrichment regressions."""

from copy import deepcopy
import importlib.util
from pathlib import Path

import pytest
import yaml


EIC = Path(__file__).resolve().parents[1] / "examples" / "EIC"
spec = importlib.util.spec_from_file_location(
    "eic_generator", EIC / "generate_narad_eic_instance.py"
)
generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)


def test_requested_pvs_and_semantics():
    components = [
        {"id": "inst:ES12_T1", "kind": "Kicker"},
        {"id": "inst:ES12_BPM0", "kind": "DiagnosticDevice"},
    ]
    generator.apply_eic_kind_rules(components)
    assert components[1]["kind"] == "BeamPositionMonitor"
    assert components[1]["functions"] == ["BeamPositionMeasurement"]
    signals, bindings = generator.generate_epics_signals(components)
    signals = {s["id"].removeprefix("inst:"): s for s in signals}
    assert set(signals) == {
        "es12-t1:PS:H:Status", "es12-t1:PS:H:Current-SP", "es12-t1:PS:H:Current-RB",
        "es12-t1:PS:V:Status", "es12-t1:PS:V:Current-SP", "es12-t1:PS:V:Current-RB",
        "es12-t1:PS:H:Current-SP.DRVL", "es12-t1:PS:H:Current-SP.DRVH",
        "es12-t1:PS:V:Current-SP.DRVL", "es12-t1:PS:V:Current-SP.DRVH",
        "es12-bpm0:X-RB", "es12-bpm0:Y-RB",
    }
    for name, signal in signals.items():
        assert signal["source_system"] == "EPICS"
        assert signal["access_protocol"] == "EPICS PVAccess"
        assert signal["native_unit"] == (
            "A" if "Current" in name else "none" if "Status" in name else "mm"
        )
        assert signal["signal_role"] == (
            "RangeLimit" if ".DRV" in name else
            "Status" if "Status" in name else "Setpoint" if name.endswith("-SP") else "Readback"
        )
        if ".DRV" in name:
            assert signal["native_data_type"] == "Float"
            assert signal["canonical_signal_type"] == "MagnetCurrentRange"
            assert signal["quantity_kind"] == "ElectricCurrent"
            binding = next(b for b in bindings if b["object"] == signal["id"])
            assert binding["predicate"] == "pals:has_limit_signal"
            assert binding["subject"] == "inst:ES12_T1"
            limit = "min" if name.endswith(".DRVL") else "max"
            assert signal["alias"] == [
                f"{'horizontal' if ':H:' in name else 'vertical'}_current_{limit}"
            ]
    assert len(bindings) == 12
    assert {b["subject"] for b in bindings} == {c["id"] for c in components}
    assert {b["object"] for b in bindings} == {f"inst:{name}" for name in signals}


def test_occurrences_share_pvs_and_unrelated_elements_are_ignored():
    components = [
        {"id": f"inst:es12_t1_{i:03}", "kind": "Kicker"} for i in (1, 2)
    ] + [
        {"id": "inst:ES12_T1_EXTRA", "kind": "Kicker"},
        {"id": "inst:ES12_Q0", "kind": "Quadrupole"},
    ]
    signals, bindings = generator.generate_epics_signals(components)
    assert len(signals) == 10
    assert len(bindings) == len({b["id"] for b in bindings}) == 20


def test_full_example_is_reproducible_and_preserves_skeleton():
    skeleton = yaml.safe_load(generator.DEFAULT_INPUT.read_text())
    original = deepcopy(skeleton)
    enriched = generator.enrich_document(skeleton)
    assert skeleton == original
    assert enriched == yaml.safe_load(generator.DEFAULT_OUTPUT.read_text())
    facility = enriched["facility"]
    assert len(facility["signals"]) == len(facility["signal_bindings"]) == 2304
    component_ids = {c["id"] for c in facility["components"]}
    signal_ids = {s["id"] for s in facility["signals"]}
    assert all(b["subject"] in component_ids and b["object"] in signal_ids
               for b in facility["signal_bindings"])
    with pytest.raises(ValueError, match="empty signals"):
        generator.enrich_document(enriched)
