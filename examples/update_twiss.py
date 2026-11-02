#!/usr/bin/env python3
"""Merge s positions and Twiss parameters from a Bmad table into a NARAD skeleton.

Columns are identified by the table header, in any order. Columns named for
NARAD TwissP fields are imported; other columns are ignored. Existing TwissP
fields absent from the table (or marked ``---``) are preserved.

Only matching YAML components are updated; unmatched table rows are ignored.
Repeated names are matched in occurrence order, ignoring case.
Supply ``--input`` and ``--twiss`` explicitly. The input is updated in place
unless ``--output`` specifies a separate file.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import re
from typing import Any, Optional

import yaml

from narad.datamodel import narad_pydantic as narad_model


TWISS_COLUMNS = {
    name for name, field in narad_model.TwissParamGroup.model_fields.items()
    if field.annotation == Optional[float]
}


@dataclass(frozen=True)
class TwissRow:
    name: str
    s_position: float
    twiss: dict[str, float]


def read_twiss_table(path: Path) -> list[TwissRow]:
    """Read the main lattice rows, excluding the trailing Lord Elements table."""
    rows: list[TwissRow] = []
    columns: list[str] | None = None
    with path.open(encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            if line.strip() == "Lord Elements:":
                break
            fields = line.strip().removeprefix("#").split()
            if not fields:
                continue
            header = [field.casefold() for field in fields]
            if "name" in header and "s" in header:
                if len(set(header)) != len(header):
                    raise ValueError(f"{path}:{line_number}: duplicate column names")
                columns = header
                continue
            if line.lstrip().startswith("#"):
                continue
            if columns is None:
                raise ValueError(f"{path}:{line_number}: expected a header containing name and s")
            if len(fields) != len(columns):
                raise ValueError(
                    f"{path}:{line_number}: expected {len(columns)} columns from header, "
                    f"got {len(fields)}"
                )
            record = dict(zip(columns, fields))
            try:
                twiss = {
                    name: float(value.replace("D", "E").replace("d", "e"))
                    for name, value in record.items()
                    if name in TWISS_COLUMNS and value != "---"
                }
                s_position = float(record["s"].replace("D", "E").replace("d", "e"))
            except ValueError as error:
                raise ValueError(f"{path}:{line_number}: invalid numeric value") from error
            rows.append(
                TwissRow(
                    name=record["name"],
                    s_position=s_position,
                    twiss=twiss,
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

        if "TwissP" in model.model_fields and row.twiss:
            twiss = component.setdefault("TwissP", {})
            twiss.setdefault("id", f"{component['id']}/TwissP")
            twiss.update(row.twiss)
            twiss_count += 1

    # Catch unsupported parameter groups or malformed values before overwriting a file.
    narad_model.PALSAccelerator.model_validate(document)
    return s_count, twiss_count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--twiss", type=Path, required=True, help="Bmad Twiss table")
    parser.add_argument("--input", type=Path, required=True, help="input NARAD YAML")
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
