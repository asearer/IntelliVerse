"""
Test suite for Event Bus stubs.
"""

from orchestration.event_bus.kafka_producer import KafkaProducerStub
from orchestration.event_bus.kafka_consumer import KafkaConsumerStub

def test_event_publish_and_consume():
    producer = KafkaProducerStub()
    consumer = KafkaConsumerStub()
    producer.publish("test_topic", {"msg": "hello"})
    messages = consumer.consume("test_topic")
    assert isinstance(messages, list)
