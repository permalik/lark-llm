import json

from kafka import KafkaProducer


def inference_result():
    producer = KafkaProducer(
        bootstrap_servers=["localhost:9092"],
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
    topic = "inference.result"
    message = {"id": 1, "content": "Hello from Python producer"}
    producer.send(topic, message)
    producer.flush()
