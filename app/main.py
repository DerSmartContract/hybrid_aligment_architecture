
"""
main.py – FastAPI-Schnittstelle für das Hybrid-Alignment-System

Diese Datei bietet eine einfache HTTP-API zur Bewertung von Texten gemäß Verfassung sowie zur Agenten-Feedback-Aggregation.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from app.core.evaluation import ConstitutionEvaluator
from app.core.meta_scoring import aggregate_scores
from app.schemas.feedback import AgentFeedback
from typing import List

app = FastAPI(title="Hybrid Alignment API", version="1.0")

evaluator = ConstitutionEvaluator()

class TextInput(BaseModel):
    text: str

@app.post("/evaluate")
def evaluate_text(input: TextInput):
    """
    Bewertet Text anhand der Verfassung.
    """
    return evaluator.evaluate_text(input.text)

@app.post("/meta/aggregate")
def aggregate_feedback(feedbacks: List[AgentFeedback]):
    """
    Aggregiert epistemische Bewertungen mehrerer Agenten.
    """
    return aggregate_scores(feedbacks)