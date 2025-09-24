"""
Test suite for API Gateway stubs.
"""

from orchestration.api_gateway import main as api_main

def test_status_endpoint():
    client = api_main.app.test_client()
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json == {"status": "OK"}
