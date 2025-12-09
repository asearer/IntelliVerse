"""
Test suite for AI Core Prediction Service.
"""

import pytest
import os
import shutil
from ai_core.services.prediction_service import AICoreStub

# Fixture to clean up model file after tests
@pytest.fixture(scope="module", autouse=True)
def cleanup_model():
    yield
    if os.path.exists("ai_core/models/classifier.pkl"):
        # We might want to keep it, but for pure testing usually we clean.
        # However, for this demo flow, we might keep it. 
        # Let's just pass.
        pass

def test_ai_prediction_output() -> None:
    """
    Ensure AICoreStub.predict returns a dictionary with all expected keys and correct types.
    """
    ai = AICoreStub()
    # Pass valid feature vector (4 features as per training in init)
    data = {"features": [0.5, 1.2, 0.3, 0.9]}
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
