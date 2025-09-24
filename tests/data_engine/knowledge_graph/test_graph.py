"""
Test suite for Data Engine Knowledge Graph stubs.
"""

from data_engine.knowledge_graph.graph_builder import KnowledgeGraphStub

def test_add_and_query_data():
    kg = KnowledgeGraphStub()
    data = {"node": "test"}
    kg.add_data(data)
    result = kg.query("node")
    assert isinstance(result, list)
