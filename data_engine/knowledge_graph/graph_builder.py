"""
Knowledge Graph Stub
"""

class KnowledgeGraphStub:
    """
    Adds data and allows querying.
    """

    def __init__(self):
        self.store = []
        print("[KnowledgeGraph] Initialized Stub")

    def add_data(self, data):
        self.store.append(data)
        print(f"[KnowledgeGraph] Added data: {data}")

    def query(self, key):
        """
        Returns all nodes containing the key.
        """
        results = [d[key] for d in self.store if key in d]
        print(f"[KnowledgeGraph] Query for {key}: {results}")
        return results
