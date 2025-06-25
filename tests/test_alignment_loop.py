"""
test_alignment_loop.py – Basistests für das Hybrid-Alignment-System
"""
from app.core.evaluation import ConstitutionEvaluator
from app.core.meta_scoring import aggregate_scores
from app.schemas.feedback import AgentFeedback

def test_constitution_evaluation():
    evaluator = ConstitutionEvaluator()
    result = evaluator.evaluate_text("Das System darf niemals lügen und muss ehrlich bleiben.")
    assert "compliance_score" in result
    assert isinstance(result["compliance_score"], float)
    assert 0.0 <= result["compliance_score"] <= 1.0

def test_meta_scoring_aggregation():
    feedbacks = [
        AgentFeedback(agent_name="A", content="ok", epistemic_score=0.6),
        AgentFeedback(agent_name="B", content="ok", epistemic_score=0.8),
        AgentFeedback(agent_name="C", content="ok", epistemic_score=0.4)
    ]
    result = aggregate_scores(feedbacks)
    assert "avg_score" in result
    assert "variance" in result
    assert "confidence" in result
    assert 0.0 <= result["avg_score"] <= 1.0