"""
Data Analytics Anomaly Detection.

Detects statistical anomalies in data streams using Z-Score Analysis.
"""

from typing import Dict, Any, List, Union
import numpy as np
from utils.logger import setup_logger

logger = setup_logger(__name__)

class DataAnomalyDetectionStub:
    """
    detects anomalies in numerical data streams.
    
    Maintains a rolling window of history to calculate mean and std dev.
    """

    def __init__(self, window_size: int = 50) -> None:
        """
        Initialize Anomaly Detector.
        
        Args:
            window_size: Number of historical points to keep for statistics.
        """
        self.window_size = window_size
        self.history: List[List[float]] = []
        logger.info(f"Anomaly Detection Service initialized (Window: {window_size}).")

    def analyze(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze incoming data for anomalies.
        
        Args:
            data: Data dictionary containing 'sensor_data' (list of floats).
            
        Returns:
            Dict: Analysis result containing 'is_anomaly' flag and 'details'.
        """
        sensor_values = data.get("sensor_data")
        
        if not sensor_values or not isinstance(sensor_values, list):
            logger.warning("Invalid data format for anomaly detection.")
            return {"is_anomaly": False, "reason": "Invalid Data"}
            
        # Update history
        self.history.append(sensor_values)
        if len(self.history) > self.window_size:
            self.history.pop(0)
            
        if len(self.history) < 5:
            # Need some history to have stats
            return {"is_anomaly": False, "status": "Initializing"}
            
        # Calculate Z-Scores
        history_np = np.array(self.history)
        mean = np.mean(history_np, axis=0)
        std = np.std(history_np, axis=0)
        
        # Avoid division by zero
        std[std == 0] = 1.0
        
        current = np.array(sensor_values)
        z_scores = np.abs((current - mean) / std)
        
        # Threshold (e.g., 3 sigma)
        threshold = 2.5 
        anomalies = z_scores > threshold
        
        if np.any(anomalies):
            logger.warning(f"Anomaly detected! indices: {np.where(anomalies)[0]}, z-scores: {z_scores[anomalies]}")
            return {
                "is_anomaly": True,
                "anomalous_indices": np.where(anomalies)[0].tolist(),
                "severity": "High" if np.max(z_scores) > 4.0 else "Medium"
            }
            
        return {"is_anomaly": False, "status": "Normal"}
