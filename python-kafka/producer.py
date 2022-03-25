from datetime import datetime
import json
from kafka import KafkaProducer
from kafka.errors import *
import random
import time
import uuid


producer = KafkaProducer(
   value_serializer=lambda msg: json.dumps(msg).encode('utf-8'), # we serialize our data to json for efficent transfer
   bootstrap_servers=['ec2-44-202-5-136.compute-1.amazonaws.com:9092'])

TOPIC_NAME = 'hmv-anwers'


def _produce_event():
    """
    Function to produce events
    """
    # UUID produces a universally unique identifier
    return {
            "data": {'event_id': str(uuid.uuid4()),
                     'event_datetime': datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),
                     'message': 'message-sent'
                     },
            "metadata": {
                "timestamp": datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),
                "record-type": "data",
                "operation": "update",
                "partition-key-type": "schema-table",
                "schema-name": "client",
                "table-name": "chatbot-answers",
                "transaction-id": str(uuid.uuid4())[0:5],
            }
        }

def send_events():
    while(True):
        data = _produce_event()
        try:
            time.sleep(2) # simulate some processing logic
            future = producer.send(TOPIC_NAME, value=data)
            print(data)
            assert future.succeeded
        except Exception as e:
            print("KafkaLogsProducer exception sending log to Kafka: %s", e)
            raise Exception("KafkaLogsProducer exception sending log to Kafka: %s" % e)

if __name__ == '__main__':
    send_events()
