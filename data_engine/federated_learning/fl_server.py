"""
Federated Learning Server Stub.

Aggregates model updates from clients using Federated Averaging (FedAvg).
"""

from typing import Dict, List, Any
import numpy as np
from utils.logger import setup_logger

logger = setup_logger(__name__)

class FLServerStub:
    """
    Simulated Federated Learning Server.
    
    Collects gradient/model updates and computes the weighted average.
    """

    def __init__(self) -> None:
        """Initialize FL Server."""
        self.global_model: List[float] = [0.0] * 5  # Dummy weights
        self.round_updates: List[Dict[str, Any]] = []
        logger.info("FL Server initialized.")

    def receive_update(self, client_id: int, update: Dict[str, Any]) -> None:
        """
        Receive model update from a client.

        Args:
            client_id: ID of the client.
            update: The update payload containing 'model_update' list.
        """
        weights = update.get("model_update")
        if not weights:
            logger.warning(f"Received empty update from Client {client_id}")
            return
            
        self.round_updates.append(update)
        logger.info(f"Received update from Client {client_id}")
        
        # In a real system, we'd wait for N clients. Here, we update immediately for demo.
        self._aggregate_updates()

    def _aggregate_updates(self) -> None:
        """
        Perform FedAvg on collected updates.
        
        New Global Weight = Average(Client Weights)
        """
        if not self.round_updates:
            return

        logger.info("Aggregating updates (FedAvg)...")
        num_updates = len(self.round_updates)
        new_weights = np.zeros_like(self.global_model)
        
        for update in self.round_updates:
            new_weights += np.array(update["model_update"])
            
        self.global_model = (new_weights / num_updates).tolist()
        self.round_updates = [] # Reset for next round
        
        logger.info(f"Global model updated. New weights: {self.global_model}")
