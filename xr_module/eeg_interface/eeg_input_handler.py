"""
EEG Input Handler Stub
"""

class EEGStub:
    """
    Returns cognitive state dictionary with keys 'stress_level' and 'attention_level'.
    """

    def capture_cognitive_state(self):
        """
        Stub method for cognitive state capture.
        """
        state = {
            "stress_level": 0.5,
            "attention_level": 0.8
        }
        print(f"[XR EEG] Captured Cognitive State: {state}")
        return state
