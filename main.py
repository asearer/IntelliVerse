"""
IntelliVerse Main Entrypoint.

Purpose:
- Serves as a central orchestrator for all IntelliVerse modules.
- Demonstrates stub interactions between AI Core, Robotics, XR, Web3, Data Engine, and Security.
- Can be extended to full production workflows.

Usage:
    python3 main.py
"""

from utils.logger import setup_logger
from utils.config import config
from orchestration.api_gateway.main import app as api_app
from ai_core.services.prediction_service import AICoreStub
from ai_core.explainability.shap_analysis import ExplainabilityStub
from ai_core.explainability.lime_analysis import LIMEStub
from robotics_iot.swarm.swarm_controller import RoboticsStub
from xr_module.gesture_recognition.gesture_controller import XRStub
from xr_module.eeg_interface.eeg_input_handler import EEGStub
from web3_module.backend.api import Web3Stub
from data_engine.ingestion.pipeline import DataEngineStub
from data_engine.federated_learning.fl_client import FLClientStub
from data_engine.federated_learning.fl_server import FLServerStub
from data_engine.knowledge_graph.graph_builder import KnowledgeGraphStub
from data_engine.analytics.anomaly_detection import DataAnomalyDetectionStub
from security_monitoring.anomaly_detection import AnomalyDetectionStub

logger = setup_logger(__name__)

def run_demo() -> None:
    """
    Demonstrate an end-to-end flow between modules.

    Initializes all system stubs and simulates a complete data flow cycle:
    ingestion -> prediction -> explanation -> human input -> execution ->
    learning -> analytics -> security -> logging.
    """
    logger.info(f"=== {config.APP_NAME} Demo Starting on {config.ENV} ===")

    try:
        # Initialize modules
        # 1. AI & Data
        ai_core = AICoreStub()
        data_engine = DataEngineStub()
        
        # 2. Advanced Analysis
        shap_expl = ExplainabilityStub()
        lime_expl = LIMEStub()
        
        # 3. Physical & XR
        robotics = RoboticsStub()
        xr = XRStub()
        eeg = EEGStub()
        
        # 4. Distributed Systems
        web3 = Web3Stub()
        fl_client = FLClientStub(client_id=1)
        fl_server = FLServerStub()
        
        # 5. Monitoring
        kg = KnowledgeGraphStub()
        analytics = DataAnomalyDetectionStub()
        security = AnomalyDetectionStub()

        # --- FLOW EXECUTION ---

        # Simulate data ingestion
        data = data_engine.ingest_data()
        
        # Extract features for prediction (assuming data contains raw + assets)
        # In a real pipeline, we'd have a Transformer here.
        # For this demo, we extract the numeric sensor data.
        prediction_input = {"features": data.get("sensor_data", [])}
        
        kg.add_data(data)

        # AI Prediction
        prediction = ai_core.predict(prediction_input)
        shap_expl.explain(prediction)
        
        # LIME might need raw data, passing prediction for stub compatibility
        lime_expl.explain(prediction)

        # Human-in-the-loop input
        gesture_feedback = xr.capture_gesture_input()
        eeg_state = eeg.capture_cognitive_state()

        # Robotics execution based on prediction and user input
        # Logic: If risky, ask for confirmation (simulated here)
        command = {
            "action": "move" if prediction.get("predicted_label") == 0 else "scan", 
            "target_id": 0,
            "risk_score": prediction.get("risk_score")
        }
        
        robotics.execute_command(command)

        # Federated learning update
        update = fl_client.local_train()
        fl_server.receive_update(client_id=1, update=update)

        # Analytics
        analytics.analyze(data)

        # Security monitoring
        security.detect(prediction)

        # Blockchain logging
        web3.log_to_blockchain({"prediction": prediction, "gesture": gesture_feedback})

        logger.info(f"=== {config.APP_NAME} Demo Complete ===")

    except Exception as e:
        logger.critical(f"Critical error during execution: {e}", exc_info=True)
        raise

if __name__ == "__main__":
    # Optionally start API Gateway in background
    # api_app.run(port=5000)
    
    run_demo()
