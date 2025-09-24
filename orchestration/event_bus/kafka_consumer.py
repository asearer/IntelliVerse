"""
Kafka Consumer Stub
"""

class KafkaConsumerStub:
    """
    Consumes events.
    """

    def consume(self, topic):
        print(f"[EventBus] Consuming from topic '{topic}'")
        return []
