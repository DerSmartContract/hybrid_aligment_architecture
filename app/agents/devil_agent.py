
"""
devil_agent.py – Der Devil's Advocate Agent

Ziel: Aufdeckung von Schwächen, Inkonsistenzen oder potenziellen Exploits in generierten Antworten.
Der Agent agiert absichtlich konträr und adversarial zur Prüfung der Robustheit.
"""

from typing import List
from app.schemas.feedback import AgentFeedback

class DevilAgent:
    def __init__(self):
        self.name = "DevilAgent"

    def critique(self, candidate: str, context: str = "") -> AgentFeedback:
        """
        Generiert eine gezielte, konträre Kritik zur getesteten Antwort.
        """
        # Pseudo-kritisches Regelwerk (ersetzbar durch LLM oder Regeln)
        if "immer" in candidate.lower():
            issue = "Generalisierung: Absolutismen wie 'immer' sind oft angreifbar."
            score = 0.2
        elif "nicht möglich" in candidate.lower():
            issue = "Negativitätsbias: Möglicherweise übersehenes Potenzial."
            score = 0.3
        else:
            issue = "Kein offensichtlicher Exploit, aber formale Gegenposition kann simuliert werden."
            score = 0.5

        return AgentFeedback(
            agent_name=self.name,
            content=f"Kritikpunkt: {issue}",
            epistemic_score=score
        )