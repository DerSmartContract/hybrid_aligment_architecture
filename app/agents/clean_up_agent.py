
"""
clean_up_agent.py – Der Aufräum-Agent

Entfernt überflüssige, inkonsistente oder schwache Beiträge aus dem Multi-Agent-Feedback. 
Sorgt für Klarheit und Robustheit in der Argumentationsbasis des Systems.
"""

from typing import List
from app.schemas.feedback import AgentFeedback

class CleanUpAgent:
    def __init__(self, min_epistemic_threshold: float = 0.3):
        self.name = "CleanUpAgent"
        self.threshold = min_epistemic_threshold

    def filter_feedback(self, feedbacks: List[AgentFeedback]) -> List[AgentFeedback]:
        """
        Entfernt alle Feedback-Einträge mit epistemischer Bewertung unterhalb der Schwelle.
        """
        cleaned = [f for f in feedbacks if f.epistemic_score >= self.threshold]
        return cleaned