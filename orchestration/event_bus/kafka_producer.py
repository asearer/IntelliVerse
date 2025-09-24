"""
Kafka Producer Stub
"""

class KafkaProducerStub:
    """
    Publishes events.
    """

    def publish(self, topic, message):
        print(f"[EventBus] Publishing to topic '{topic}': {message}")
