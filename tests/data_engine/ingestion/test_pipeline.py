"""
Test suite for Data Engine ingestion pipeline stubs.
"""

from data_engine.ingestion.pipeline import DataEngineStub

def test_data_ingestion_returns_dict():
    pipeline = DataEngineStub()
    data = pipeline.ingest_data()
    assert isinstance(data, dict)
