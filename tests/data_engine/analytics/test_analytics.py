"""
Test suite for Data Analytics Anomaly Detection.
"""

import pytest
from data_engine.analytics.anomaly_detection import DataAnomalyDetectionStub

def test_analyze_returns_result() -> None:
    """
    Verify anomaly detection logic returns structured result.
    """
    detector = DataAnomalyDetectionStub(window_size=10)
    
    # Normal data stream
    normal_data = {"sensor_data": [10.0, 10.0, 10.0, 10.0]}
    
    # Feed explicit normal data to build history
    for _ in range(6):
        detector.analyze(normal_data)
        
    result = detector.analyze(normal_data)
    assert not result["is_anomaly"]
    
    # Feed anomaly (spike)
    anomaly_data = {"sensor_data": [50.0, 10.0, 10.0, 10.0]}
    
    result = detector.analyze(anomaly_data)
    
    # Logic note: With history of [10, 10, ...], 50 is (50-10)/0 = inf? 
    # Logic std handles 0 -> 1. so Z = 40. > 2.5
    assert result["is_anomaly"] is True
    assert 0 in result["anomalous_indices"]
