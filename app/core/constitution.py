
"""
constitution.py – Laden und Bereitstellen der YAML-Verfassung

Dieses Modul liest die Core-Constitution-Datei ein, validiert sie und stellt strukturierte Zugriffspunkte bereit.
"""

import yaml
from pathlib import Path
from typing import Dict, Any

CONSTITUTION_PATH = Path(__file__).parent.parent.parent / "constitution" / "core_constitution.yaml"

def load_constitution() -> Dict[str, Any]:
    """
    Lädt und gibt die YAML-Verfassung als Python-Dictionary zurück.
    """
    try:
        with open(CONSTITUTION_PATH, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            assert "prinzipien" in data, "Verfassung muss 'prinzipien' enthalten"
            return data
    except Exception as e:
        raise RuntimeError(f"Fehler beim Laden der Verfassung: {e}")