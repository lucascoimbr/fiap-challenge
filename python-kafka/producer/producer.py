import json
from bson import json_util

from kafka import KafkaProducer

import random

producer = KafkaProducer(
    bootstrap_servers=['52.201.234.137:9092'],
    value_serializer=lambda v: str(v).encode('utf-8'))

# for i in range(10):
#     data = { 'tag ': 'blah',
#         'name' : 'sam',
#         'index' : i,
#         'score': 
#             {'row1': 100,
#              'row2': 200
#         }
#     }   
#     producer.send('kafka-python-topic', json.dumps(data, default=json_util.default).encode('utf-8'))

while True:
    producer.send('kafka-python-topic', random.randint(1,10))

