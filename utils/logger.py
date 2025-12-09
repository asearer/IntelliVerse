"""
Logging Utility Module.

Provides a configured logger instance for the application.
"""

import logging
import sys
from utils.config import config

def setup_logger(name: str) -> logging.Logger:
    """
    Configure and return a logger instance.

    Args:
        name: The name of the logger (usually __name__).

    Returns:
        logging.Logger: Configured logger.
    """
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        logger.setLevel(config.LOG_LEVEL)
        
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
    return logger
