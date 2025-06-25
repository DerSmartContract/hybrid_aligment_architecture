
"""
socratic_agent.py – Der sokratische Agent

Ziel: Förderung von Klarheit und Tiefe durch gezielte Rückfragen. 
Der Agent stellt keine Aussagen auf, sondern reflektiert durch Fragen auf Schwächen, Lücken und blinde Flecken.
"""

from app.schemas.feedback import AgentFeedback

class SocraticAgent:
    def __init__(self):
        self.name = "SocraticAgent"

    def inquire(self, candidate: str) -> AgentFeedback:
        """
        Stellt eine tiefergehende Rückfrage zur getätigten Aussage, um Reflexion anzuregen.
        """
        if "muss" in candidate.lower():
            question = "Warum genau ist das zwingend notwendig? Gibt es alternative Wege?"
            score = 0.6
        elif "immer" in candidate.lower():
            question = "Gilt das wirklich in *allen* Fällen? Was wären Ausnahmen?"
            score = 0.7
        elif "darf nicht" in candidate.lower():
            question = "Worauf basiert dieses Verbot? Könnte es sinnvolle Kontexte geben?"
            score = 0.5
        else:
            question = "Welche Annahmen liegen dieser Aussage zugrunde?"
            score = 0.5

        return AgentFeedback(
            agent_name=self.name,
            content=f"Sokratische Rückfrage: {question}",
            epistemic_score=score
        )
