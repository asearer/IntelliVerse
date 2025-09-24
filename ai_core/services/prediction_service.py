"""
AI Core Prediction Service Stub
"""

import random

class AICoreStub:
    """
    Stub for AI Core predictions.
    """

    def __init__(self):
        print("[AI Core] Initialized AI Core Stub")

    def predict(self, data):
        """
        Returns a stub prediction dictionary matching test expectations.
        Keys: 'predicted_label', 'confidence', 'metadata', 'recommended_action', 'risk_score'
        """
        prediction = {
            "predicted_label": random.choice([0, 1]),
            "confidence": round(random.random(), 2),
            "recommended_action": random.choice(["monitor", "alert", "ignore"]),
            "risk_score": round(random.random(), 3),
            "metadata": {"source": "AI Core Stub"}
        }
        print(f"[AI Core] Generated Prediction: {prediction}")
        return prediction
