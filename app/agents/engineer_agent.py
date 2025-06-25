
"""
engineer_agent.py – Der Umsetzbarkeits-/Nützlichkeits-Agent

Bewertet generierte Antworten auf Umsetzbarkeit, technische Konsistenz und potenzielle Anwendbarkeit.
Sorgt dafür, dass Vorschläge nicht nur gut argumentiert, sondern auch realisierbar sind.
"""

from app.schemas.feedback import AgentFeedback

class EngineerAgent:
    def __init__(self):
        self.name = "EngineerAgent"

    def assess(self, candidate: str) -> AgentFeedback:
        """
        Bewertet eine Aussage hinsichtlich technischer Umsetzbarkeit oder Nützlichkeit.
        """
        if any(keyword in candidate.lower() for keyword in ["nicht möglich", "theoretisch", "eventuell"]):
            note = "Eingeschränkte Umsetzbarkeit oder zu vage formuliert."
            score = 0.3
        elif "kann implementiert werden" in candidate.lower():
            note = "Konkrete Implementierung erkennbar."
            score = 0.7
        else:
            note = "Neutral – keine klare Aussage zur Umsetzbarkeit."
            score = 0.5

        return AgentFeedback(
            agent_name=self.name,
            content=f"Nützlichkeitsprüfung: {note}",
            epistemic_score=score
        )