"""
Test suite for AI Core Prediction Service stubs.
"""

import pytest
from ai_core.services.prediction_service import AICoreStub

def test_ai_prediction_output() -> None:
    """
    Ensure AICoreStub.predict returns a dictionary with all expected keys and correct types.
    """
    ai = AICoreStub()
    data = {"feature1": 0.5, "feature2": 1.2}
    prediction = ai.predict(data)
    
    # Check Type
    assert isinstance(prediction, dict), "Prediction should be a dictionary"
    
    # Check Keys
    expected_keys = {
        "predicted_label", 
        "confidence", 
        "recommended_action", 
        "risk_score", 
        "metadata"
    }
    assert expected_keys.issubset(prediction.keys()), f"Missing keys: {expected_keys - prediction.keys()}"

    # Check Value Types
    assert isinstance(prediction["predicted_label"], int)
    assert isinstance(prediction["confidence"], float)
    assert isinstance(prediction["recommended_action"], str)
    assert isinstance(prediction["risk_score"], float)
    assert isinstance(prediction["metadata"], dict)
    
    # Check Value Constraints
    assert 0 <= prediction["confidence"] <= 1.0
    assert 0 <= prediction["risk_score"] <= 1.0
    assert prediction["recommended_action"] in ["monitor", "alert", "ignore"]
