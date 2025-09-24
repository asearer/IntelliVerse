"""
Federated Learning Client Stub
"""

import random

class FLClientStub:
    """
    Stub for a federated learning client.
    """

    def __init__(self, client_id):
        self.client_id = client_id
        print(f"[FLClient] Initialized Client {client_id}")

    def local_train(self):
        """
        Returns dictionary containing 'client_id' and 'model_update'.
        """
        update = {
            "client_id": self.client_id,
            "model_update": [random.random() for _ in range(5)]
        }
        print(f"[FLClient] Client {self.client_id} generated model update: {update['model_update']}")
        return update
