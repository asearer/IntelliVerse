"""
Test suite for Data Engine Ingestion Pipeline stubs.
"""

import pytest
from typing import Dict, List, Union
from data_engine.ingestion.pipeline import DataEngineStub

def test_data_ingestion_output() -> None:
    """
    Ensure DataEngineStub.ingest_data returns a dictionary with correct structure and types.
    """
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
    assert len(data["sensor_data"]) > 0, "sensor_data should not be empty"
    assert all(isinstance(x, float) for x in data["sensor_data"]), "sensor_data should contain floats"
