"""
Knowledge Graph Query Stub

Purpose:
- Simulates querying a knowledge graph
"""

class GraphQueryStub:
    def __init__(self, graph):
        self.graph = graph

    def query(self, node_index):
        """
        Query a node's connections
        """
        if node_index < len(self.graph.nodes):
            return {"connected_nodes": [node_index]}
        return {"connected_nodes": []}
