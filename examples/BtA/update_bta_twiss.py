#!/usr/bin/env python3
"""Add s positions and Twiss parameters from a Bmad table to a BtA skeleton.

By default the script updates ``bta_narad_skeleton_palsparserpy.yaml`` in place.  Use
``--output`` to write a separate file instead.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import re
from typing import Any

import yaml

from narad.datamodel import narad_pydantic as narad_model


HERE = Path(__file__).resolve().parent
DEFAULT_TWISS = HERE / "bta_twiss.dat"
DEFAULT_SKELETON = HERE / "bta_narad_skeleton_palsparserpy.yaml"

TWISS_COLUMNS = (
    "beta_a",
    "alpha_a",
    "eta_x",
    "etap_x",
    "phi_a",
    "beta_b",
    "alpha_b",
    "eta_y",
    "etap_y",
    "phi_b",
)


@dataclass(frozen=True)
class TwissRow:
    name: str
    s_position: float
    twiss: dict[str, float]


def read_twiss_table(path: Path) -> list[TwissRow]:
    """Read the main lattice rows, excluding the trailing Lord Elements table."""
    rows: list[TwissRow] = []
    with path.open(encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            if line.strip() == "Lord Elements:":
                break
            fields = line.split()
            if not fields or fields[0].startswith("#"):
                continue
            if len(fields) != 15 or not fields[0].isdigit():
                raise ValueError(f"{path}:{line_number}: expected a 15-column Twiss row")
            try:
                values = [float(value) for value in fields[5:]]
                s_position = float(fields[3])
            except ValueError as error:
                raise ValueError(f"{path}:{line_number}: invalid numeric value") from error
            rows.append(
                TwissRow(
                    name=fields[1],
                    s_position=s_position,
                    twiss=dict(zip(TWISS_COLUMNS, values)),
                )
            )
    if not rows:
        raise ValueError(f"{path}: no Twiss rows found")
    return rows


def component_name(component: dict[str, Any]) -> str:
    return component["id"].removeprefix("inst:")


def table_name(component: dict[str, Any]) -> str:
    """Undo suffixes added by the PALS-to-NARAD component ID uniquifier."""
    name = re.sub(r"_\d{3}$", "", component_name(component))
    if component.get("kind") in {"BeginningEle", "Marker"}:
        name = re.sub(r"_B\d+$", "", name)
    return name


def add_twiss_data(document: dict[str, Any], rows: list[TwissRow]) -> tuple[int, int]:
    """Update components in lattice order and return (s count, Twiss count)."""
    rows_by_name: dict[str, list[TwissRow]] = defaultdict(list)
    for row in rows:
        rows_by_name[row.name.casefold()].append(row)

    used_by_name: dict[str, int] = defaultdict(int)
    s_count = 0
    twiss_count = 0

    for component in document["facility"]["components"]:
        lookup_name = table_name(component)
        candidates = rows_by_name.get(lookup_name.casefold(), [])
        occurrence = used_by_name[lookup_name.casefold()]
        if occurrence >= len(candidates):
            continue
        row = candidates[occurrence]
        used_by_name[lookup_name.casefold()] += 1

        model = getattr(narad_model, component["kind"])
        if "LongitudinalPlacementP" in model.model_fields:
            placement = component.setdefault(
                "LongitudinalPlacementP",
                {"id": f"{component['id']}/LongitudinalPlacementP"},
            )
            placement["s_position"] = row.s_position
            s_count += 1

        if "TwissP" in model.model_fields:
            component["TwissP"] = {
                "id": f"{component['id']}/TwissP",
                **row.twiss,
            }
            twiss_count += 1

    unmatched_rows = [
        row.name
        for name, named_rows in rows_by_name.items()
        for row in named_rows[used_by_name[name] :]
    ]
    if unmatched_rows:
        raise ValueError(
            "NARAD skeleton has no matching component(s) for Twiss rows: "
            + ", ".join(unmatched_rows)
        )

    # Catch unsupported parameter groups or malformed values before overwriting a file.
    narad_model.PALSAccelerator.model_validate(document)
    return s_count, twiss_count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--twiss", type=Path, default=DEFAULT_TWISS, help="Bmad Twiss table")
    parser.add_argument("--input", type=Path, default=DEFAULT_SKELETON, help="input NARAD skeleton")
    parser.add_argument(
        "--output",
        type=Path,
        help="output YAML (default: update --input in place)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output = args.output or args.input
    with args.input.open(encoding="utf-8") as stream:
        document = yaml.safe_load(stream)
    s_count, twiss_count = add_twiss_data(document, read_twiss_table(args.twiss))
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as stream:
        yaml.safe_dump(document, stream, sort_keys=False, allow_unicode=True, width=100)
    print(
        f"Wrote {output} with {s_count} s positions and "
        f"{twiss_count} Twiss parameter groups."
    )


if __name__ == "__main__":
    main()
