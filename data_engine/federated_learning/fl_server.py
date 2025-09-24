"""
Federated Learning Server Stub
"""

class FLServerStub:
    """
    Stub for a federated learning server.
    """

    def __init__(self):
        self.global_model = [0.0 for _ in range(5)]
        print("[FLServer] Initialized FL Server")

    def receive_update(self, client_id, update):
        """
        Combines server and client updates element-wise.
        """
        model_update = update.get("model_update", [])
        self.global_model = [(g + u)/2 for g, u in zip(self.global_model, model_update)]
        print(f"[FLServer] Updated global model with client {client_id} update: {self.global_model}")
        return None
