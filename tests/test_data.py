"""Data test."""
import os
import glob
import pytest
from pathlib import Path

from archived.narad_system.datamodel import narad_system_pydantic
from linkml_runtime.loaders import yaml_loader

DATA_DIR_VALID = Path(__file__).parent / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "invalid"

VALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_VALID, '*.yaml'))
INVALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_INVALID, '*.yaml'))


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Test loading of all valid data files."""
    tgt_class = narad_system_pydantic.NaradSystem
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj