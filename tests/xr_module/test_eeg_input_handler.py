"""
Test suite for XR EEG interface stubs.
"""

from xr_module.eeg_interface.eeg_input_handler import EEGStub

def test_capture_cognitive_state():
    """
    Ensure EEGStub returns correct keys expected by workflow.
    """
    eeg = EEGStub()
    state = eeg.capture_cognitive_state()
    assert isinstance(state, dict)
    assert "stress_level" in state
    assert "attention_level" in state
