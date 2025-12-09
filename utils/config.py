"""
Configuration Management Module.

Centralizes application configuration using environment variables and default values.
"""

import os
from dataclasses import dataclass

@dataclass
class Config:
    """
    Application Configuration.
    """
    # General
    APP_NAME: str = "IntelliVerse"
    ENV: str = os.getenv("ENV", "development")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    # AI Core
    MODEL_PATH: str = os.getenv("MODEL_PATH", "ai_core/models/classifier.pkl")
    
    # Data Engine
    DATA_PATH: str = os.getenv("DATA_PATH", "data_engine/data")
    
    # Robotics
    SWARM_SIZE: int = int(os.getenv("SWARM_SIZE", "5"))

config = Config()
