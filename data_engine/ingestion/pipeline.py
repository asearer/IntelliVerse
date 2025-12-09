"""
Data Engine Ingestion Pipeline Stub.

Purpose:
- Ingests data from multiple sources (sensors, APIs, databases)
- Prepares data for AI Core or Analytics modules
"""

import os
import pandas as pd
import numpy as np
from typing import Dict, List, Union, Any
from utils.config import config
from utils.logger import setup_logger

logger = setup_logger(__name__)

class DataEngineStub:
    """
    Data Engine Ingestion Pipeline.

    Ingests data from CSV files simulating sensor streams.
    """

    def __init__(self) -> None:
        """
        Initialize the Data Engine.
        """
        self.data_path = config.DATA_PATH
        self._ensure_dummy_data()
        logger.info("Data Engine initialized.")

    def _ensure_dummy_data(self) -> None:
        """
        Create a dummy CSV file if it doesn't exist.
        """
        os.makedirs(self.data_path, exist_ok=True)
        csv_file = os.path.join(self.data_path, "sensors.csv")
        
        if not os.path.exists(csv_file):
            logger.info("Generating dummy sensor data...")
            df = pd.DataFrame(np.random.rand(10, 4), columns=["temp", "vib", "pressure", "humidity"])
            df.to_csv(csv_file, index=False)
            logger.info(f"Dummy data saved to {csv_file}")

    def ingest_data(self) -> Dict[str, Union[List[float], str]]:
        """
        Ingest data from the local CSV file.

        Returns:
            Dict[str, Union[List[float], str]]: A dictionary containing:
                - 'sensor_data' (List[float]): A list of one row of sensor values.
                - 'satellite_image' (str): Path or identifier for the satellite image.
        """
        csv_file = os.path.join(self.data_path, "sensors.csv")
        try:
            df = pd.read_csv(csv_file)
            # Sample one random row to simulate extraction
            sample = df.sample(1).iloc[0].tolist()
            logger.info(f"Ingested sample: {sample}")
            
            return {
                "sensor_data": sample,
                "satellite_image": "assets/sat_001.png"
            }
        except Exception as e:
            logger.error(f"Failed to ingest data: {e}")
            return {
                "sensor_data": [0.0, 0.0, 0.0, 0.0],
                "satellite_image": "error"
            }
