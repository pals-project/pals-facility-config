import subprocess
import sys
from pathlib import Path

import palsparserpy as pp
import pytest
import yaml

from narad.datamodel import narad_pydantic as narad_model
from translators.palsparserpy_to_narad import (
    component_functions,
    component_model,
    magnetic_multipoles,
    translatable_component_models,
)


EXAMPLES_DIR = Path(__file__).resolve().parents[1] / "examples"
PALS_INPUTS_DIR = EXAMPLES_DIR / "pals_inputs"
FODO_FILE = PALS_INPUTS_DIR / "fodo.pals.yaml"
IOTA_FILE = PALS_INPUTS_DIR / "iota.pals.yaml"
BTA_FILE = PALS_INPUTS_DIR / "bta.pals.yaml"
MULTIPASS_FILE = Path(__file__).with_name("review_multipass.pals.yaml")
CONVERT_FILE = Path(__file__).with_name("convert.pals.yaml")
EX_FILE = Path(__file__).with_name("ex.pals.yaml")
TRANSLATOR = (
    Path(__file__).resolve().parents[1]
    / "src"
    / "translators"
    / "palsparserpy_to_narad.py"
)
CUSTOM_TRANSLATOR = TRANSLATOR.with_name("pals_to_narad.py")


def _single_expanded_line(path: Path):
    lattices = pp.parse_and_expand_pals(path, problems="none")
    lattice_names = lattices.expanded.keys()
    assert len(lattice_names) == 1

    lattice = lattices.expanded[lattice_names[0]]
    branches = lattice["branches"]
    assert len(branches) == 1

    branch = branches[0]
    branch_name = branch.keys()[0]
    return lattices, branch[branch_name]["line"]


def test_fodo_lattice_is_parsed_and_expanded() -> None:
    _, line = _single_expanded_line(FODO_FILE)

    element_names = [entry.keys()[0] for entry in line]
    fodo_cell = ["drift1", "quad1", "drift2", "quad2", "drift1"]

    assert element_names == fodo_cell * 3
    assert line[3]["quad2"]["MagneticMultipoleP"]["Bn1"].as_float() == -1.0


def test_iota_lattice_expands_reversed_beamline() -> None:
    lattices, line = _single_expanded_line(IOTA_FILE)
    element_names = [entry.keys()[0] for entry in line]

    assert lattices.problems == []
    assert len(element_names) == 102
    assert element_names[0] == "begin"
    assert element_names[1:] == list(reversed(element_names[1:]))


def test_custom_translator_uses_only_selected_iota_lattice_branch(
    tmp_path: Path,
) -> None:
    output = tmp_path / "iota_narad.yaml"
    subprocess.run(
        [
            sys.executable,
            str(CUSTOM_TRANSLATOR),
            "-input",
            str(IOTA_FILE),
            "-output",
            str(output),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    facility = yaml.safe_load(output.read_text(encoding="utf-8"))["facility"]

    assert [beamline["id"] for beamline in facility["beamlines"]] == [
        "inst:IOTA_RING"
    ]
    assert len(facility["components"]) == 102
    assert len(facility["component_relations"]) == 101


def test_bta_lattice_is_parsed_and_expanded() -> None:
    lattices, line = _single_expanded_line(BTA_FILE)
    element_names = [entry.keys()[0] for entry in line]

    assert lattices.problems == []
    assert len(element_names) == 163
    assert {"dh1t", "dh23t"}.isdisjoint(element_names)
    assert element_names[0] == "beginning_b1"
    assert element_names[-1] == "end_b0"
    assert "mw006" in element_names


def test_bta_twiss_update_matches_current_lattice(tmp_path: Path) -> None:
    output = tmp_path / "bta_with_twiss.yaml"
    subprocess.run(
        [sys.executable, str(EXAMPLES_DIR.parent / "src/translators/update_twiss.py"),
         "--input", str(EXAMPLES_DIR.parent / ".local/translation/skeletons/bta_narad_skeleton_palsparserpy.yaml"),
         "--twiss", str(EXAMPLES_DIR.parent / "src/translators/resources/bta_twiss.dat"),
         "--output", str(output)],
        check=True, capture_output=True, text=True,
    )
    document = yaml.safe_load(output.read_text())
    components = document["facility"]["components"]
    assert len(components) == 163
    assert {"inst:DH1T", "inst:DH23T"}.isdisjoint(c["id"] for c in components)
    dh1b = next(c for c in components if c["id"] == "inst:DH1B")
    assert dh1b["LongitudinalPlacementP"]["s_position"] == 6.592
    assert "beta_a" in dh1b["TwissP"]


def test_translator_derives_multipass_and_reports_unsupported_elements(
    tmp_path: Path,
) -> None:
    output = tmp_path / "review_multipass_narad.yaml"
    result = subprocess.run(
        [
            sys.executable,
            str(TRANSLATOR),
            "-input",
            str(MULTIPASS_FILE),
            "-output",
            str(output),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    document = yaml.safe_load(output.read_text(encoding="utf-8"))
    facility = document["facility"]

    assert "version" not in document
    assert "created_date" not in document
    assert "change_log" not in document

    assert facility["beamlines"][0]["multipass"] is True
    solenoid = next(
        component
        for component in facility["components"]
        if component["kind"] == "Solenoid"
    )
    assert solenoid["SolenoidP"]["Bsol"] == 0.5
    assert "unresolved_placeholder (Placeholder)" in result.stderr
    assert "multipass identity and relationships are not yet defined" in result.stderr
    assert len(facility["component_relations"]) == 2


def test_translator_reports_unresolved_line_reference(tmp_path: Path) -> None:
    output = tmp_path / "convert_narad.yaml"
    result = subprocess.run(
        [
            sys.executable,
            str(TRANSLATOR),
            "-input",
            str(CONVERT_FILE),
            "-output",
            str(output),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    document = yaml.safe_load(output.read_text(encoding="utf-8"))
    bend = next(
        component
        for component in document["facility"]["components"]
        if component["id"] == "inst:S1"
    )

    assert "patch1 (unresolved reference)" in result.stderr
    assert bend["BendP"]["Bn0_ref"] == 1.2


def test_ex_lattice_translates_includes_inheritance_and_repeats(
    tmp_path: Path,
) -> None:
    output = tmp_path / "ex_narad.yaml"
    result = subprocess.run(
        [
            sys.executable,
            str(TRANSLATOR),
            "-input",
            str(EX_FILE),
            "-output",
            str(output),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    document = yaml.safe_load(output.read_text(encoding="utf-8"))
    facility = document["facility"]
    components = {component["id"]: component for component in facility["components"]}

    assert facility["beamlines"][0]["id"] == "inst:INJ_LINE"
    assert facility["beamlines"][0]["multipass"] is True
    assert list(components) == [
        "inst:THINGZ",
        "inst:Q1A",
        "inst:DH1A_001",
        "inst:PUEH001_001",
        "inst:QUAD1_001",
        "inst:DH1A_002",
        "inst:PUEH001_002",
        "inst:QUAD1_002",
    ]
    assert components["inst:THINGZ"]["kind"] == "Sextupole"
    assert components["inst:Q1A"]["LongitudinalPlacementP"]["length"] == pytest.approx(
        1.079360186305116e-08
    )
    assert components["inst:QUAD1_001"]["MagneticMultipoleP"]["mag_components"] == [
        {"order": 1, "Bn": 1.0}
    ]
    assert len(facility["component_relations"]) == 7
    assert "multipass identity and relationships are not yet defined" in result.stderr


def test_magnetic_multipoles_preserve_integrated_strengths_and_tilt() -> None:
    converted = magnetic_multipoles(
        {"Kn2": 4.0, "tilt3": 0.7, "Bn3L": 32.0, "Bs3L": 10.0}
    )

    assert converted == {
        "mag_components": [
            {"order": 2, "Kn": 4.0},
            {"order": 3, "tilt": 0.7, "BnL": 32.0, "BsL": 10.0},
        ]
    }


def test_magnetic_multipoles_reject_mixed_strength_types_per_order() -> None:
    with pytest.raises(ValueError, match="order 1.*Kn, KsL"):
        magnetic_multipoles({"Kn1": 1.0, "Ks1L": 2.0})


def test_component_kind_resolution_uses_schema_mappings() -> None:
    assert component_model("Instrument") is narad_model.DiagnosticDevice


def test_every_translatable_component_has_a_default_function() -> None:
    missing = [
        model.__name__
        for model in translatable_component_models()
        if component_functions(model) is None
    ]

    assert missing == []


def test_monitor_default_functions_are_specific() -> None:
    assert component_functions(narad_model.BeamPositionMonitor) == [
        "BeamPositionMeasurement"
    ]
    assert component_functions(narad_model.BeamProfileMonitor) == [
        "BeamProfileMeasurement"
    ]


def test_inherited_and_overridden_default_functions() -> None:
    assert component_functions(narad_model.ACKicker) == ["Steering"]
    assert component_functions(narad_model.Aperture) == ["Measurement"]
    assert component_functions(narad_model.NormalConductingRFCavity) == [
        "BeamAcceleration"
    ]
    assert component_functions(narad_model.BookkeepingComponent) == ["Mark"]
    assert component_functions(narad_model.BeamLineSection) == ["BeamLineSection"]
    assert component_model("RFCavity") is narad_model.RFCavity
    assert component_model("NotANaradComponent") is None
