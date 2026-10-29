"""Booster ADO naming and instance enrichment regressions."""

from copy import deepcopy
import importlib.util
from pathlib import Path

import pytest
import yaml


BOOSTER = Path(__file__).resolve().parents[1] / "examples" / "Booster"
spec = importlib.util.spec_from_file_location(
    "booster_generator", BOOSTER / "generate_narad_booster_instance.py"
)
generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)


@pytest.mark.parametrize("name, semantic, ado", [
    ("PUEHA1", "horizontal_position", "orbitData.booster:horPosA1M"),
    ("PUEVF8", "vertical_position", "orbitData.booster:verPosF8M"),
    ("puehd2_001", "horizontal_position", "orbitData.booster:horPosD2M"),
])
def test_bpm_names(name, semantic, ado):
    component = {"id": f"inst:{name}", "kind": "DiagnosticDevice"}
    generator.apply_booster_kind_rules([component])
    assert component["kind"] == "BeamPositionMonitor"
    assert component["functions"] == ["BeamPositionMeasurement"]
    assert generator.resolve_ado_names(component) == {semantic: ado}


@pytest.mark.parametrize("name, device", [
    ("DHCA1", "ba1-th-ps"),
    ("DVCF8", "bf8-tv-ps"),
    ("dhcd2_001", "bd2-th-ps"),
])
def test_corrector_names(name, device):
    assert generator.resolve_ado_names({"id": f"inst:{name}", "kind": "Kicker"}) == {
        "magnet_status": f"{device}:stateS",
        "current_range": f"{device}:rangeC",
        "current_setpoint": f"{device}:setpointsM",
        "current_readback": f"{device}:currentM",
    }


@pytest.mark.parametrize("name, kind", [
    ("PUEHG1", "DiagnosticDevice"), ("PUEHA9", "DiagnosticDevice"),
    ("PUEHA1_EXTRA", "DiagnosticDevice"), ("DHD1_EXTRA", "Bend"),
    ("IJKDHD1", "Kicker"), ("DHCA1_EXTRA", "Kicker"),
    ("DHCA1", "Quadrupole"),
])
def test_unrelated_devices_have_no_signals(name, kind):
    component = {"id": f"inst:{name}", "kind": kind}
    generator.apply_booster_kind_rules([component])
    assert generator.resolve_ado_names(component) == {}


def test_repeated_occurrences_share_signals_but_keep_bindings():
    components = [
        {"id": f"inst:DHCA1_{i:03}", "kind": "Kicker"} for i in (1, 2)
    ]
    signals, bindings = generator.generate_ado_signals(components)
    assert len(signals) == 4
    assert len(bindings) == 8
    assert len({b["id"] for b in bindings}) == 8


@pytest.mark.parametrize("kind, prefix, supply", [
    ("Quadrupole", "Q", "b-qtrim"),
    ("Sextupole", "S", "Booster.b-chrom"),
])
def test_series_magnets_share_supply_signals_per_plane(kind, prefix, supply):
    components = [
        {"id": f"inst:{prefix}{name}", "kind": kind}
        for name in ("HA1", "HF7", "va1", "VF8")
    ]
    signals, bindings = generator.generate_ado_signals(components)
    # Check the plane-specific supplies separately from the common main supply.
    signals = [s for s in signals if not s["id"].startswith("inst:bmm.control:")]
    bindings = [b for b in bindings if not b["object"].startswith("inst:bmm.control:")]
    assert {s["id"] for s in signals} == {
        f"inst:{supply}{plane}-ps:{attribute}"
        for plane in ("h", "v")
        for attribute in ("stateS", "rangeC", "setpointsAvgM", "currentAvgM")
    }
    assert len(signals) == 8
    assert len(bindings) == 16
    objects_by_subject = {
        c["id"]: {b["object"] for b in bindings if b["subject"] == c["id"]}
        for c in components
    }
    assert objects_by_subject[f"inst:{prefix}HA1"] == objects_by_subject[f"inst:{prefix}HF7"]
    assert objects_by_subject[f"inst:{prefix}va1"] == objects_by_subject[f"inst:{prefix}VF8"]
    assert objects_by_subject[f"inst:{prefix}HA1"].isdisjoint(objects_by_subject[f"inst:{prefix}va1"])


def test_main_dipole_range_layout_and_shared_bindings():
    components = [
        {"id": f"inst:{name}", "kind": "Bend"} for name in ("DHD2", "DHA8", "dhf2")
    ]
    signals, bindings = generator.generate_ado_signals(components)
    assert len(signals) == 4
    by_id = {s["id"]: s for s in signals}
    assert set(by_id) == {
        f"inst:bmm.control:{attribute}" for attribute in (
            "stateM", "currentRangeC", "psiCurrentSetpointAvgM", "dcctCurrentOutputAvgM",
        )
    }
    for attribute, role in (
        ("psiCurrentSetpointAvgM", "Setpoint"), ("dcctCurrentOutputAvgM", "Readback"),
    ):
        assert by_id[f"inst:bmm.control:{attribute}"]["signal_role"] == role
        assert by_id[f"inst:bmm.control:{attribute}"]["native_unit"] == "A"
    signal = by_id["inst:bmm.control:currentRangeC"]
    assert signal["id"] == "inst:bmm.control:currentRangeC"
    assert signal["canonical_signal_type"] == "MagnetCurrentRange"
    assert signal["native_data_type"] == "FloatArray"
    assert signal["native_unit"] == "none"  # Raw array contains mixed quantities.
    metadata = {m["key"]: m["value"] for m in signal["MetaP"]["additional_metadata"]}
    assert metadata["array_length"] == "6"
    assert metadata["array_order"].split(",") == [
        "setpoint", "status", "reference", "B field", "DC Current Transformer", "error",
    ]
    assert metadata["current_range_unit"] == "A"
    assert metadata["current_range_order"] == "minimum,maximum"
    raw = [6000, 65535, 6000, 19000, 6000, 60]
    assert [float(metadata["current_range_minimum"]),
            raw[int(metadata["current_range_maximum_index"])]] == [0, 6000]
    assert {b["subject"] for b in bindings} == {c["id"] for c in components}
    assert len(bindings) == 12
    for component in components:
        assert {b["object"] for b in bindings if b["subject"] == component["id"]} == set(by_id)
    # Other magnets retain their two-entry [maximum, minimum] layout.
    regular = generator.ADO_SIGNAL_SPECS["current_range"]
    assert regular["native_unit"] == "A"
    assert regular["MetaP"]["additional_metadata"][1]["value"] == "2"


def test_booster_enrichment_preserves_skeleton_and_validates():
    skeleton = yaml.safe_load((BOOSTER / "booster_narad_skeleton_palsparserpy.yaml").read_text())
    original = deepcopy(skeleton)
    document = generator.enrich_document(skeleton)
    assert skeleton == original
    facility = document["facility"]
    assert len(facility["signals"]) == 288
    quadrupoles = [
        c for c in facility["components"]
        if c["kind"] == "Quadrupole"
        and generator.re.fullmatch(r"Q[HV][A-F][1-8]", generator.device_name(c))
    ]
    dipoles = [
        c for c in facility["components"]
        if c["kind"] == "Bend"
        and generator.re.fullmatch(r"DH[A-F][1-8]", generator.device_name(c))
    ]
    sextupoles = [
        c for c in facility["components"]
        if c["kind"] == "Sextupole"
        and generator.re.fullmatch(r"S[HV][A-F][1-8]", generator.device_name(c))
    ]
    assert len(facility["signal_bindings"]) == 276 + 4 * (
        2 * len(quadrupoles) + len(dipoles) + len(sextupoles)
    )
    signals = {signal["id"]: signal for signal in facility["signals"]}
    assert signals["inst:orbitData.booster:horPosD2M"]["native_unit"] == "mm"
    assert signals["inst:bd2-th-ps:setpointsM"]["native_unit"] == "A"
    for before, after in zip(original["facility"]["components"], facility["components"]):
        for field in ("TwissP", "MagneticMultipoleP", "LongitudinalPlacementP"):
            assert before.get(field) == after.get(field)
    for binding in facility["signal_bindings"]:
        assert binding["object"] in signals
    with pytest.raises(ValueError, match="empty signals"):
        generator.enrich_document(document)


def test_stopband_supplies_are_additional_and_polarity_is_supply_specific():
    components = [
        {"id": f"inst:{name}", "kind": "Sextupole"}
        for name in ("SHC8", "SHF8", "SHB4", "SHE4", "SHA1")
    ]
    generator.add_polarity_metadata(components)
    signals, bindings = generator.generate_ado_signals(components)
    assert len(signals) == 12  # Four main and eight stopband signals.
    assert len(bindings) == 36
    expected = {
        "SHC8": ("b-sxr1-ps", "1"), "SHF8": ("b-sxr1-ps", "-1"),
        "SHB4": ("b-sxr2-ps", "-1"), "SHE4": ("b-sxr2-ps", "1"),
    }
    for component in components[:4]:
        name = generator.device_name(component)
        supply, polarity = expected[name]
        meta = {m["key"]: m["value"] for m in component["MetaP"]["additional_metadata"]}
        assert meta["stopband_supply"] == supply
        assert meta["stopband_current_polarity"] == polarity
        objects = {b["object"] for b in bindings if b["subject"] == component["id"]}
        assert objects == {
            f"inst:{device}:{attribute}"
            for device in ("Booster.b-chromh-ps", supply)
            for attribute in ("stateS", "rangeC", "setpointsAvgM", "currentAvgM")
        }
    assert "MetaP" not in components[-1]


def test_quadrupoles_have_main_and_trim_supplies_with_scoped_polarity():
    components = [
        {"id": "inst:QHA1", "kind": "Quadrupole"},
        {"id": "inst:QVA1", "kind": "Quadrupole"},
        {"id": "inst:DHA1", "kind": "Bend"},
    ]
    generator.add_polarity_metadata(components)
    signals, bindings = generator.generate_ado_signals(components)
    assert len(signals) == 12  # Four main signals shared with the dipole.
    assert len(bindings) == 20
    main_ids = {s["id"] for s in signals if s["id"].startswith("inst:bmm.control:")}
    assert len(main_ids) == 4
    for component, plane, polarity in zip(components[:2], ("h", "v"), ("1", "-1")):
        meta = {e["key"]: e["value"] for e in component["MetaP"]["additional_metadata"]}
        assert meta["trim_supply"] == f"b-qtrim{plane}-ps"
        assert meta["trim_current_polarity"] == polarity
        assert meta["main_supply"] == "bmm.control"
        targets = {b["object"] for b in bindings if b["subject"] == component["id"]}
        assert main_ids <= targets
        assert len(targets) == 8
    assert "MetaP" not in components[-1]


def test_backleg_supplies_are_additional_and_match_only_five_dipoles():
    components = [
        {"id": f"inst:{name}", "kind": "Bend"}
        for name in ("DHC7", "DHD1", "DHD4", "DHD7", "dhe1", "DHD2")
    ]
    signals, bindings = generator.generate_ado_signals(components)
    assert len(signals) == 24  # Four shared main signals plus five backleg supplies.
    assert len(bindings) == 44
    for component in components:
        name = generator.device_name(component).upper()
        targets = {b["object"] for b in bindings if b["subject"] == component["id"]}
        assert len(targets) == (4 if name == "DHD2" else 8)
        if name != "DHD2":
            device = f"Booster.b{name[2:].lower()}-blw-ps"
            assert {f"inst:{device}:{a}" for a in (
                "stateS", "rangeC", "setpointsAvgM", "currentAvgM",
            )} <= targets
    backleg_range = next(s for s in signals if s["id"] == "inst:Booster.bd1-blw-ps:rangeC")
    assert backleg_range["native_unit"] == "A"
    meta = {e["key"]: e["value"] for e in backleg_range["MetaP"]["additional_metadata"]}
    assert meta["array_length"] == "2"
    assert meta["array_order"] == "maximum,minimum"
