

"""
feedback.py – Datenmodell für Agentenfeedback

Dieses Schema beschreibt, wie Agenten Rückmeldungen im Alignment-System abgeben.
"""

from pydantic import BaseModel, Field

class AgentFeedback(BaseModel):
    agent_name: str = Field(..., description="Name des bewertenden Agenten")
    content: str = Field(..., description="Kritik, Rückfrage oder Bewertungstext des Agenten")
    epistemic_score: float = Field(..., ge=0.0, le=1.0, description="Grad des epistemischen Vertrauens [0.0–1.0]")