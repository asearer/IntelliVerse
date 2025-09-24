"""
Test suite for AI Core Explainability stubs (SHAP and LIME).
"""

import pytest
from ai_core.explainability.shap_analysis import ExplainabilityStub
from ai_core.explainability.lime_analysis import LIMEStub

def test_shap_explain():
    explainer = ExplainabilityStub()
    result = explainer.explain({"predicted_label": 1})
    assert isinstance(result, dict)
    assert "shap_values" in result

def test_lime_explain():
    explainer = LIMEStub()
    result = explainer.explain({"predicted_label": 1})
    assert isinstance(result, dict)
    assert "lime_explanation" in result
