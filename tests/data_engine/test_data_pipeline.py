"""
Test suite for Data Engine Ingestion Pipeline.
"""

import pytest
import shutil
import os
# from data_engine.ingestion.pipeline import DataEngineStub
# Wait, I must check the import path. The file is in 'data_engine'.

from typing import Dict, List, Union
# Correct import path based on file structure
from data_engine.ingestion.pipeline import DataEngineStub

def test_data_ingestion_output() -> None:
    """
    Ensure DataEngineStub.ingest_data returns a dictionary with correct structure and types.
    """
    # Clean up any existing data to ensure clean state or just let it create
    if os.path.exists("data_engine/data/sensors.csv"):
        os.remove("data_engine/data/sensors.csv")
        
    engine = DataEngineStub()
    data = engine.ingest_data()

    # Check Type
    assert isinstance(data, dict), "Ingested data should be a dictionary"

    # Check Keys
    expected_keys = {"sensor_data", "satellite_image"}
    assert expected_keys.issubset(data.keys()), f"Missing keys: {expected_keys - data.keys()}"

    # Check Value Types
    assert isinstance(data["sensor_data"], list), "sensor_data should be a list"
    assert isinstance(data["satellite_image"], str), "satellite_image should be a string"

    # Check Content Constraints
    assert len(data["sensor_data"]) == 4, "sensor_data should have 4 features"
    assert all(isinstance(x, float) for x in data["sensor_data"]), "sensor_data should contain floats"
