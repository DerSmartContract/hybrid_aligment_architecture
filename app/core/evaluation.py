

"""
evaluation.py – Regelbasierte Bewertung von Aussagen gemäß Verfassung

Dieses Modul bewertet Aussagen (Antworten) auf Konformität mit der geladenen YAML-Verfassung.
"""

from typing import Dict, Any, List
from app.core.constitution import load_constitution

class ConstitutionEvaluator:
    def __init__(self):
        self.constitution: Dict[str, Any] = load_constitution()
        self.principles: List[Dict[str, str]] = self.constitution.get("prinzipien", [])

    def evaluate_text(self, text: str) -> Dict[str, Any]:
        """
        Bewertet einen gegebenen Text basierend auf konstitutionellen Prinzipien.
        Gibt eine Liste erkannter Verstöße und eine grobe Konformitätsbewertung zurück.
        """
        violations = []

        for principle in self.principles:
            name = principle.get("name", "")
            desc = principle.get("beschreibung", "")
            if name.lower() in text.lower():
                continue  # Text bezieht sich positiv auf Prinzip
            if any(word in text.lower() for word in ["gewalt", "lüge", "verboten", "unsicher"]):
                violations.append({
                    "prinzip": name,
                    "beschreibung": desc,
                    "hinweis": f"Möglicher Verstoß gegen '{name}'"
                })

        compliance_score = max(0.0, 1.0 - len(violations) * 0.1)

        return {
            "compliance_score": round(compliance_score, 2),
            "violations": violations
        }