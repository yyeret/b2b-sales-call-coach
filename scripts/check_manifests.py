#!/usr/bin/env python3
"""Validate Claude and Codex plugin/marketplace manifests stay in sync."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

MANIFESTS = {
    "claude_plugin": ROOT / ".claude-plugin" / "plugin.json",
    "claude_marketplace": ROOT / ".claude-plugin" / "marketplace.json",
    "codex_plugin": ROOT / ".codex-plugin" / "plugin.json",
    "codex_marketplace": ROOT / ".agents" / "plugins" / "marketplace.json",
}


def main() -> int:
    data = {}
    for key, path in MANIFESTS.items():
        if not path.exists():
            print(f"ERROR: Missing manifest: {path}")
            return 1
        try:
            data[key] = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            print(f"ERROR: Invalid JSON in {path}: {exc}")
            return 1

    cp = data["claude_plugin"]
    cm = data["claude_marketplace"]
    xp = data["codex_plugin"]
    xm = data["codex_marketplace"]

    errors = []

    if cm.get("name") != xm.get("name"):
        errors.append(f"Marketplace name mismatch: {cm.get('name')} != {xm.get('name')}")

    cm_entry = (cm.get("plugins") or [{}])[0]
    xm_entry = (xm.get("plugins") or [{}])[0]

    for field in ("name", "version", "description"):
        vals = {
            "claude_plugin": cp.get(field),
            "claude_marketplace": cm_entry.get(field),
            "codex_plugin": xp.get(field),
            "codex_marketplace": xm_entry.get(field),
        }
        if len(set(vals.values())) != 1:
            errors.append(f"Field '{field}' mismatch across manifests: {vals}")

    skills_path = xp.get("skills")
    if not skills_path or not (ROOT / skills_path).is_dir():
        errors.append(f"Codex plugin 'skills' path missing or not a directory: {skills_path}")

    if not (xp.get("interface") or {}).get("displayName"):
        errors.append("Codex plugin missing interface.displayName")

    if "$schema" in xm:
        errors.append("Codex marketplace must not include '$schema' key")

    if errors:
        for err in errors:
            print(f"ERROR: {err}")
        return 1

    print("OK: All four plugin/marketplace manifests parse and agree.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
