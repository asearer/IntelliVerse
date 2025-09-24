"""
SQL Connector Stub

Purpose:
- Simulates fetching data from SQL databases
"""

class SQLConnectorStub:
    def __init__(self, connection_string="stub_connection"):
        print(f"[SQL Connector] Initialized with connection: {connection_string}")

    def fetch_data(self, query="SELECT * FROM stub_table"):
        """
        Simulate fetching data
        """
        return [{"id": 1, "value": 0.5}, {"id": 2, "value": 0.8}]
