#!/usr/bin/env python3
"""
Transform original_GUN_thru_MV.narad_v_dm.yaml  →  narad_SOSA_SNN_schema.yaml

Mapping rules
─────────────
Source root key                         → narad_system.yaml slot
─────────────────────────────────────────────────────────────────
narad                                   → narad_config
narad.capability_layer.profiles         → narad_config.capability_layer.profiles
  <family>.kind                         → device_domain  (rename key)
  <family>.magnet_type_profiles / …     → type_profiles  (rename key)
  <profile>.kind                        → device_type    (rename key)
  <tsc>.class                           → capability_class (rename key)
narad.facility                          → narad_config.facility
narad.control_system                    → narad_config.control_system
narad.signal_layer                      → narad_config.signal_layer
  signal_definitions keys               → type_signal_sets dict
    <key>.<signal>.epics_suffix         → control_system_suffix (rename key)
beamlines[i].GUN_thru_MV / …           → beamlines[i] with beamline_name key
elements[i].narad.signal_bindings       → instance_signal_bindings list
  <signal_name>: {pv: …, facility: …}  → InstanceSignalBinding entry
elements[i].RFP / BendP / Magnetic…    → param_set list (named blocks)
elements[i].FacilityParams             → facility_param_set
elements[i].JLabP  (old name)          → facility_param_set  (alias)
elements[i].length                      → length
elements[i].kind                        → element_kind
"""

import sys
from pathlib import Path
import ruamel.yaml
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap

yaml = YAML()
yaml.preserve_quotes = True
yaml.default_flow_style = False
yaml.width = 120

# ── helpers ─────────────────────────────────────────────────────────────────

def _rename(d: dict, old: str, new: str) -> None:
    """Rename a key in-place, preserving order."""
    if old in d:
        d[new] = d.pop(old)


def _copy_comment(src, dst):
    """Best-effort: ruamel carries comments with the node, no action needed."""
    pass


# ── capability layer ─────────────────────────────────────────────────────────

PROFILE_COLLECTION_KEYS = {
    "magnet_type_profiles",
    "instrument_type_profiles",
    "cavity_type_profiles",
    "type_profiles",          # already correct
}


def transform_signal(sig: dict) -> dict:
    """No change needed for signals; return as-is."""
    return sig


def transform_type_specific_capability(tsc: dict) -> dict:
    _rename(tsc, "class", "capability_class")
    if "signals" in tsc:
        tsc["signals"] = [transform_signal(s) for s in tsc["signals"]]
    return tsc


def transform_capability(cap: dict) -> dict:
    if "signals" in cap:
        cap["signals"] = [transform_signal(s) for s in cap["signals"]]
    return cap


def transform_profile(profile: dict) -> dict:
    _rename(profile, "kind", "device_type")
    if "type_specific_capabilities" in profile:
        profile["type_specific_capabilities"] = [
            transform_type_specific_capability(t)
            for t in profile["type_specific_capabilities"]
        ]
    return profile


def transform_profile_family(family: dict) -> dict:
    _rename(family, "kind", "device_domain")
    # normalise profile collection key → type_profiles
    for old_key in PROFILE_COLLECTION_KEYS - {"type_profiles"}:
        if old_key in family:
            family["type_profiles"] = family.pop(old_key)
            break
    if "shared_capabilities" in family:
        for cap_name, cap_body in family["shared_capabilities"].items():
            transform_capability(cap_body)
    if "type_profiles" in family:
        for prof_name, prof_body in family["type_profiles"].items():
            transform_profile(prof_body)
    # drop graph_projection (not in narad_system.yaml schema)
    family.pop("graph_projection", None)
    return family


def transform_capability_layer(cl: dict) -> dict:
    if "profiles" in cl:
        for fam_name, fam_body in cl["profiles"].items():
            transform_profile_family(fam_body)
    # drop default_graph_projection if present
    cl.pop("default_graph_projection", None)
    return cl


# ── signal layer ─────────────────────────────────────────────────────────────

def transform_signal_definitions(sd: dict) -> dict:
    """
    Normalise signal_definitions to type_signal_sets keyed by device type/domain.

    Old format keys and their mapping:
      shared_magnet_signals  → flat {signal: binding}  → Magnet device key
      magnet_type_signals    → nested {DeviceType: {signal: binding}}  → pass through
      instrument_type_signals→ nested {DeviceType: {signal: binding}}  → pass through
      cavity_signals         → flat {signal: binding}  → RFCavity device key

    New format:
      type_signal_sets       → already keyed by device type/domain
    """
    # Map from old group key → target device key when the group is a flat signal dict
    FLAT_GROUP_TO_DEVICE = {
        "shared_magnet_signals": "Magnet",
        "cavity_signals": "RFCavity",
    }
    # Groups whose values are nested {DeviceType: {signal: binding}}
    NESTED_GROUPS = {"magnet_type_signals", "instrument_type_signals"}

    # Already in new format?
    if "type_signal_sets" in sd:
        tss = sd["type_signal_sets"]
        for _dev, bindings in tss.items():
            for _sig, bdata in bindings.items():
                _rename(bdata, "epics_suffix", "control_system_suffix")
        result = CommentedMap()
        result["type_signal_sets"] = tss
        return result

    new_tss = CommentedMap()

    for group_key, group_val in sd.items():
        if not isinstance(group_val, dict):
            continue
        if group_key in FLAT_GROUP_TO_DEVICE:
            dev_key = FLAT_GROUP_TO_DEVICE[group_key]
            if dev_key not in new_tss:
                new_tss[dev_key] = CommentedMap()
            for sig_name, sig_body in group_val.items():
                new_tss[dev_key][sig_name] = sig_body
                _rename(new_tss[dev_key][sig_name], "epics_suffix", "control_system_suffix")
        elif group_key in NESTED_GROUPS:
            # values are {DeviceType: {signal: binding}}
            for dev_key, signals in group_val.items():
                if dev_key not in new_tss:
                    new_tss[dev_key] = CommentedMap()
                for sig_name, sig_body in signals.items():
                    new_tss[dev_key][sig_name] = sig_body
                    _rename(new_tss[dev_key][sig_name], "epics_suffix", "control_system_suffix")

    result = CommentedMap()
    result["type_signal_sets"] = new_tss
    return result


def transform_facility(fac: dict) -> dict:
    if "signal_definitions" in fac:
        fac["signal_definitions"] = transform_signal_definitions(fac["signal_definitions"])
    fac.pop("identifier", None)   # not in narad_system.yaml FacilityConfig
    return fac


def transform_signal_layer(sl: dict) -> dict:
    if "facilities" in sl:
        for fac_name, fac_body in sl["facilities"].items():
            transform_facility(fac_body)
    return sl


# ── narad_config (top-level narad block) ─────────────────────────────────────

def transform_narad_config(cfg: dict) -> dict:
    cfg.pop("intent", None)
    if "capability_layer" in cfg:
        transform_capability_layer(cfg["capability_layer"])
    if "signal_layer" in cfg:
        transform_signal_layer(cfg["signal_layer"])
    return cfg


# ── beamlines ────────────────────────────────────────────────────────────────

def transform_beamlines(beamlines_raw) -> list:
    """
    Source beamlines may be:
      - list of {name: …, kind: …, line: […]}          (example_narad_UITF)
      - list of {GUN_thru_MV: {kind: …, line: […]}}    (original_GUN_thru_MV)
    Output: list of {beamline_name: …, beamline_kind: …, line: […]}
    """
    result = []
    for entry in beamlines_raw:
        bl = CommentedMap()
        if "beamline_name" in entry:
            # Already example_narad_UITF style
            bl["beamline_name"] = entry["beamline_name"]
            bl["beamline_kind"] = entry.get("kind", "BeamLine")
            bl["line"] = entry.get("line", [])
        elif "name" in entry:
            bl["beamline_name"] = entry["name"]
            bl["beamline_kind"] = entry.get("kind", "BeamLine")
            bl["line"] = entry.get("line", [])
        else:
            # dict key is the beamline name
            for bl_name, bl_body in entry.items():
                bl["beamline_name"] = bl_name
                bl["beamline_kind"] = bl_body.get("kind", "BeamLine")
                bl["line"] = bl_body.get("line", [])
                break
        result.append(bl)
    return result


# ── elements ─────────────────────────────────────────────────────────────────

PHYSICS_PARAM_BLOCKS = {
    "RFP":               ["frequency", "voltage", "phase"],
    "BendP":             ["angle_ref", "e1", "e2"],
    "MagneticMultipoleP":["Kn1"],
    "SolenoidP":         ["Ksol"],
}

# Capability class for each signal name
SIGNAL_CAPABILITY_CLASS = {
    # Magnet shared (MagnetCapability)
    "current_setpoint":  "narad:MagnetCapability",
    "current_readback":  "narad:MagnetCapability",
    "current_min":       "narad:MagnetCapability",
    "current_max":       "narad:MagnetCapability",
    # Type-specific magnet
    "strength_setpoint": "narad:QuadrupoleCapability",
    "kick_setpoint":     "narad:CorrectorCapability",
    "field_setpoint":    "narad:DipoleCapability",
    # Instrument
    "horizontal_beam_position": "narad:BPMCapability",
    "vertical_beam_position":   "narad:BPMCapability",
    # RF Cavity
    "gradient_setpoint": "narad:CavityGradientCapability",
    "gradient_readback": "narad:CavityGradientCapability",
    # status is shared — use a generic fallback
    "status":            "narad:SystemCapability",
}


def transform_element(elem: dict) -> dict:
    out = CommentedMap()

    # name / kind / length
    out["name"] = elem["name"]
    out["element_kind"] = elem.get("kind", elem.get("element_kind", ""))
    if "length" in elem:
        out["length"] = elem["length"]

    # narad block → capability_profile_family, capability_profile, instance_signal_bindings
    narad_block = elem.get("narad", {})
    if narad_block:
        if "capability_profile_family" in narad_block:
            out["capability_profile_family"] = narad_block["capability_profile_family"]
        if "capability_profile" in narad_block:
            out["capability_profile"] = narad_block["capability_profile"]

        signal_bindings_raw = narad_block.get("signal_bindings", {})
        if signal_bindings_raw:
            isb_list = []
            for sig_name, sb in signal_bindings_raw.items():
                isb = CommentedMap()
                isb["name"] = sig_name
                isb["pv_name"] = sb.get("pv", "")
                cap_class = SIGNAL_CAPABILITY_CLASS.get(sig_name, "narad:SystemCapability")
                isb["is_instance_of"] = [cap_class]
                facility = sb.get("facility", "")
                control_system = sb.get("control_system", "")
                if facility:
                    isb["is_hosted_by"] = [f"narad:{facility}"]
                if control_system:
                    isb["is_property_of"] = f"narad:{control_system}"
                isb_list.append(isb)
            out["instance_signal_bindings"] = isb_list

    # physics param blocks → param_set list
    param_set_list = []
    for block_name, field_names in PHYSICS_PARAM_BLOCKS.items():
        if block_name in elem:
            raw = elem[block_name]
            block = CommentedMap()
            block["name"] = block_name
            for field in field_names:
                if field in raw:
                    block[field] = raw[field]
            param_set_list.append(block)
    if param_set_list:
        out["param_set"] = param_set_list

    # FacilityParams / JLabP → facility_param_set
    fp_raw = elem.get("FacilityParams", elem.get("JLabP", None))
    if fp_raw:
        fp = CommentedMap()
        # JLabP uses jlab_type; FacilityParams uses facility_element_type
        fp["facility_element_type"] = fp_raw.get(
            "facility_element_type", fp_raw.get("jlab_type", "")
        )
        if "modeled_as" in fp_raw:
            fp["modeled_as"] = fp_raw["modeled_as"]
        if "properties" in fp_raw:
            fp["properties"] = fp_raw["properties"]
        out["facility_param_set"] = fp

    return out


def transform_elements(elements_raw: list) -> list:
    return [transform_element(e) for e in elements_raw]


# ── main ─────────────────────────────────────────────────────────────────────

def transform(src_path: Path, dst_path: Path) -> None:
    with src_path.open("r", encoding="utf-8") as fh:
        src = yaml.load(fh)

    out = CommentedMap()

    # ── narad_config ──────────────────────────────────────────────────────────
    if "narad" in src:
        cfg = src["narad"]
        transform_narad_config(cfg)
        out["narad_config"] = cfg
    elif "narad_config" in src:
        cfg = src["narad_config"]
        transform_narad_config(cfg)
        out["narad_config"] = cfg

    # ── beamlines ─────────────────────────────────────────────────────────────
    if "beamlines" in src:
        out["beamlines"] = transform_beamlines(src["beamlines"])

    # ── elements ──────────────────────────────────────────────────────────────
    if "elements" in src:
        out["elements"] = transform_elements(src["elements"])

    with dst_path.open("w", encoding="utf-8") as fh:
        yaml.dump(out, fh)

    print(f"Written: {dst_path}  ({dst_path.stat().st_size:,} bytes)")


if __name__ == "__main__":
    base = Path(__file__).parent
    src = base / "original_GUN_thru_MV.narad_v_dm.yaml"
    dst = base / "narad_SOSA_SNN_schema.yaml"
    transform(src, dst)
