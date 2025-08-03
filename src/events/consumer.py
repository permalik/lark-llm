import json

from kafka import KafkaConsumer

from events import producer
from gemma import essence


def inference_request():
    consumer = KafkaConsumer(
        "inference.request",
        bootstrap_servers=["localhost:9092"],
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="llm-llm",
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    )

    for msg in consumer:
        print("Raw string:", msg.value)
        producer.inference_result()
        response = essence.generate_response("user", "Why is the sky blue?")
        print(response)
