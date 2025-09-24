"""
Test suite for Security Monitoring anomaly detection stubs.
"""

from security_monitoring.anomaly_detection import AnomalyDetectionStub

def test_detect_method():
    security = AnomalyDetectionStub()
    result = security.detect({"prediction": 1})
    assert result is None
