"""
Test suite for Knowledge Graph stub.
"""

import pytest
from data_engine.knowledge_graph.graph_builder import KnowledgeGraphStub

def test_add_and_query_data() -> None:
    """
    Verify graph node addition and querying.
    """
    kg = KnowledgeGraphStub()
    
    # Add generic data (node creation)
    data1 = {"type": "sensor", "value": 0.5}
    kg.add_data(data1)
    
    # Add explicit node
    kg.add_node("sensor_01", {"type": "sensor", "location": "lab"})
    
    # Query by key presence
    results = kg.query("type")
    
    assert len(results) >= 2 # At least the two we added
    assert any(r["value"] == 0.5 for r in results)
    assert any(r.get("location") == "lab" for r in results)
    
    # Test edges (graph structure)
    kg.add_node("server_01", {"type": "server"})
    kg.add_edge("sensor_01", "server_01")
    
    assert "server_01" in kg.adj_list["sensor_01"]

