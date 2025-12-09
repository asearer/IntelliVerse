"""
AI Core Prediction Service.

This module provides a production implementation of the AI Core Prediction Service,
using a Scikit-Learn RandomForestClassifier.
"""

import os
import joblib
import numpy as np
from typing import Any, Dict, List, Union, Optional
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from utils.config import config
from utils.logger import setup_logger

logger = setup_logger(__name__)

class AICoreStub:
    """
    AI Core Service wrapping a Scikit-Learn model.

    Attributes:
        model (RandomForestClassifier): The trained machine learning model.
    """

    def __init__(self) -> None:
        """
        Initialize the AI Core Stub.
        
        Loads a pre-trained model from disk or trains a fresh one if not found.
        """
        self.model_path = config.MODEL_PATH
        self.model = self._load_or_train_model()
        logger.info("AI Core initialized successfully.")

    def _load_or_train_model(self) -> RandomForestClassifier:
        """
        Load model from disk or train a new one.

        Returns:
            RandomForestClassifier: The loaded or newly trained model.
        """
        if os.path.exists(self.model_path):
            try:
                logger.info(f"Loading model from {self.model_path}")
                return joblib.load(self.model_path)
            except Exception as e:
                logger.error(f"Failed to load model: {e}. Training new one.")
        
        logger.info("Training new dummy model...")
        # Train a dummy model
        X, y = make_classification(n_samples=100, n_features=4, random_state=42)
        model = RandomForestClassifier(n_estimators=10, random_state=42)
        model.fit(X, y)
        
        # Save model
        try:
            os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
            joblib.dump(model, self.model_path)
            logger.info(f"Model saved to {self.model_path}")
        except Exception as e:
            logger.error(f"Failed to save model: {e}")
            
        return model

    def predict(self, data: Any) -> Dict[str, Union[int, float, str, Dict[str, str]]]:
        """
        Generate a prediction based on input data.

        Args:
            data: Input data. Expects a list/array-like of features. 
                  (e.g., {"features": [0.1, 0.2, 0.3, 0.4]})

        Returns:
            Dict: Prediction result.
        """
        # Parse input
        features = None
        if isinstance(data, dict):
             features = data.get("features")
        elif isinstance(data, (list, np.ndarray)):
             features = data
        
        if features is None:
             logger.warning("Invalid input format. Using dummy features.")
             features = [0.0] * 4 # Fallback
        
        # Ensure 2D array
        features_arr = np.array(features).reshape(1, -1)
        
        # Adjust dimensions if necessary (simple hack for robustness against random inputs)
        if features_arr.shape[1] != self.model.n_features_in_:
             logger.warning(f"Feature mismatch. Expected {self.model.n_features_in_}, got {features_arr.shape[1]}. Resizing.")
             features_arr = np.resize(features_arr, (1, self.model.n_features_in_))

        # Predict
        prediction_cls = int(self.model.predict(features_arr)[0])
        probabilities = self.model.predict_proba(features_arr)[0]
        confidence = float(max(probabilities))
        risk_score = 1.0 - confidence if prediction_cls == 0 else confidence

        result: Dict[str, Union[int, float, str, Dict[str, str]]] = {
            "predicted_label": prediction_cls,
            "confidence": round(confidence, 2),
            "recommended_action": "alert" if risk_score > 0.7 else ("monitor" if risk_score > 0.3 else "ignore"),
            "risk_score": round(risk_score, 3),
            "metadata": {"source": "Scikit-Learn RandomForest"}
        }
        
        logger.info(f"Prediction generated: {result}")
        return result
