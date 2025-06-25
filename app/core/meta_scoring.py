"""
meta_scoring.py – Metabewertung von Agentenfeedback

Dieses Modul aggregiert Rückmeldungen verschiedener Agenten, berechnet Durchschnittswerte
und identifiziert Konsens oder starke Abweichungen im epistemischen Vertrauen.
"""

from typing import List, Dict
from app.schemas.feedback import AgentFeedback

def aggregate_scores(feedbacks: List[AgentFeedback]) -> Dict[str, float]:
    """
    Aggregiert epistemische Scores der Agenten und berechnet Mittelwert, Varianz und Konfidenz.
    """
    if not feedbacks:
        return {"avg_score": 0.0, "variance": 0.0, "confidence": 0.0}

    scores = [f.epistemic_score for f in feedbacks]
    avg_score = sum(scores) / len(scores)
    variance = sum((s - avg_score) ** 2 for s in scores) / len(scores)
    confidence = max(0.0, 1.0 - variance)  # Hohe Varianz → niedrige Konfidenz

    return {
        "avg_score": round(avg_score, 3),
        "variance": round(variance, 3),
        "confidence": round(confidence, 3)
    }
