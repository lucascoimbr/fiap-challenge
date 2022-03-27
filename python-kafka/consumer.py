from kafka import KafkaConsumer
import transforms.base as bt
from transforms.flat import flatten_records as flattening
from transforms.date import format_date_records as format_date
from transforms.number import format_number_records as format_number
from datetime import datetime
import ast
import json

TOPIC_NAME = 'hmv-anwers'

consumer = KafkaConsumer(
    TOPIC_NAME,
    auto_offset_reset='earliest', # where to start reading the messages at
    group_id='pipeline-1', # consumer group id
    bootstrap_servers=['localhost:29092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8')) # we deserialize our data from json
)

def consume_events():
    for records in consumer:
        print(records)

if __name__ == '__main__':
    print("Consumer working!")
    consume_events()
