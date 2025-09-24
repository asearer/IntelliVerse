"""
API Connector Stub

Purpose:
- Simulates fetching data from external APIs
"""

class APIConnectorStub:
    def __init__(self, api_url="https://stub.api"):
        print(f"[API Connector] Initialized with API URL: {api_url}")

    def fetch_data(self, endpoint="/data"):
        """
        Simulate API fetch
        """
        return {"sensor_1": 0.1, "sensor_2": 0.9, "satellite_image": "stub_path"}
