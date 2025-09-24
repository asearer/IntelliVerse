"""
Test suite for AI Core Prediction Service stubs.
"""

import pytest
from ai_core.services.prediction_service import AICoreStub

def test_ai_prediction_output():
    """
    Ensure AICoreStub.predict returns a dictionary with expected keys.
    """
    ai = AICoreStub()
    data = {"feature1": 0.5, "feature2": 1.2}
    prediction = ai.predict(data)
    assert isinstance(prediction, dict)
    assert "predicted_label" in prediction
    assert "confidence" in prediction
