"""
Test suite for XR gesture recognition stubs.
"""

from xr_module.gesture_recognition.gesture_controller import XRStub

def test_capture_gesture_input():
    xr = XRStub()
    gesture = xr.capture_gesture_input()
    assert isinstance(gesture, dict)
    assert "gesture_type" in gesture
