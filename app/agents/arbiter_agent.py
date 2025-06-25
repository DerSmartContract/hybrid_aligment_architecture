"""
arbiter_agent.py – Der Schiedsrichter-Agent (Arbiter)

Bewertet Konflikte zwischen Agentenmeinungen, trifft Meta-Entscheidungen und führt Konsensentscheidungen herbei.
Er dient als letzte Instanz im Multi-Agent-Critique-Prozess.
"""

from typing import List, Dict, Any
from app.schemas.feedback import AgentFeedback

class ArbiterAgent:
    def __init__(self):
        self.name = "Arbiter"

    def evaluate_conflict(self, feedbacks: List[AgentFeedback]) -> Dict[str, Any]:
        """
        Evaluierung und Auflösung von Meinungsverschiedenheiten zwischen Agenten.
        Gibt eine konsolidierte Einschätzung und einen finalen Entscheidungsvorschlag zurück.
        """
        summary = {
            "conflicting_opinions": [],
            "final_decision": None,
            "justification": ""
        }

        opinions = {f.agent_name: f.content for f in feedbacks}
        summary["conflicting_opinions"] = opinions

        # Beispiel-Logik: Priorität nach epistemischer Tiefe
        sorted_by_depth = sorted(feedbacks, key=lambda f: f.epistemic_score, reverse=True)
        if sorted_by_depth:
            top = sorted_by_depth[0]
            summary["final_decision"] = top.content
            summary["justification"] = (
                f"Entscheidung basiert auf höchster epistemischer Bewertung durch {top.agent_name} "
                f"(Score: {top.epistemic_score})."
            )

        return summary
