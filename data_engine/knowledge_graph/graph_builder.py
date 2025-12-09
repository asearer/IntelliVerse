"""
Knowledge Graph Builder Stub.

Maintains a simple in-memory property graph.
"""

from typing import Dict, Any, List, Set
from utils.logger import setup_logger

logger = setup_logger(__name__)

class KnowledgeGraphStub:
    """
    In-memory Knowledge Graph.
    
    Nodes are identified by string IDs.
    Edges are stored in an adjacency list.
    """

    def __init__(self) -> None:
        """Initialize Graph."""
        self.nodes: Dict[str, Dict[str, Any]] = {}
        self.adj_list: Dict[str, List[str]] = {}
        logger.info("Knowledge Graph initialized (Stub).")

    def add_data(self, data: Dict[str, Any]) -> None:
        """
        Ingest data as a node in the graph.
        
        Args:
            data: Data dictionary. Must contain identifying info to be useful. 
                  Here we auto-generate an ID if missing.
        """
        node_id = f"node_{len(self.nodes)}"
        self.add_node(node_id, data)
        logger.info(f"Added data as Node: {node_id}")

    def add_node(self, node_id: str, attributes: Dict[str, Any]) -> None:
        """Add a node with attributes."""
        self.nodes[node_id] = attributes
        if node_id not in self.adj_list:
            self.adj_list[node_id] = []

    def add_edge(self, source: str, target: str) -> None:
        """Add a directed edge."""
        if source in self.nodes and target in self.nodes:
            self.adj_list[source].append(target)
        else:
            logger.warning(f"Failed to add edge: {source} -> {target} (Nodes missing)")

    def query(self, key: str) -> List[Dict[str, Any]]:
        """
        Find all nodes containing a specific attribute key.
        
        Args:
            key: Attribute key to search for.

        Returns:
            List[Dict]: List of node attributes that contain the key.
        """
        results = [attrs for attrs in self.nodes.values() if key in attrs]
        logger.info(f"Query for key '{key}' returned {len(results)} nodes.")
        return results
