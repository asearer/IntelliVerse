"""
Test suite for AI Core Explainability services.
"""

import pytest
from ai_core.explainability.shap_analysis import ExplainabilityStub
from ai_core.explainability.lime_analysis import LIMEStub

def test_shap_explain() -> None:
    """
    Verify SHAP analysis generates feature importance scores.
    """
    explainer = ExplainabilityStub()
    # Mock prediction input from AICore
    prediction = {
        "predicted_label": 1,
        "confidence": 0.85,
        "risk_score": 0.15
    }
    
    explanation = explainer.explain(prediction)
    
    assert isinstance(explanation, dict)
    assert "shap_values" in explanation
    assert "base_value" in explanation
    
    shap_values = explanation["shap_values"]
    assert isinstance(shap_values, dict)
    
    # Check that we have expected sensor keys (temp, vib, etc)
    expected_features = ["temp", "vib", "pressure", "humidity"]
    for feat in expected_features:
        assert feat in shap_values
        assert isinstance(shap_values[feat], float)
        
    # Validation: Sum of values should approximate confidence (heuristic property)
    total_attribution = sum(shap_values.values())
    assert abs(total_attribution - 0.85) < 0.01

def test_lime_explain():
    explainer = LIMEStub()
    result = explainer.explain({"predicted_label": 1})
    assert isinstance(result, dict)
    assert "lime_explanation" in result
