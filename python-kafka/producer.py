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
            "Body":
{
  "protocol":"1247620220319T182215916649",
  "queryResult": {
      "allRequiredParamsPresent": "true",
      "fulfillmentMessages": "teste",
      "fulfillmentText": "Poderia informar seu CPF ou Número do Convenio?",
      "intent": {
          "displayName": "gostaria de ajuda",
          "name": "projects/newagent-uc9l/agent/intents/ae6c62e4-a8bf-4615-acbf-c104802d2002"
      },
      "intentDetectionConfidence": "0.4426844",
      "languageCode": "pt-br",
      "parameters": {
          "location": "",
          "url": ""
      },
      "queryText": "estou come duvidas sobre agendamento de consultas"
  },
  "responseId": "g6e6c10e-5a35-4809-9883-773437533ff9-40ef389b"
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
