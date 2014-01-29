# -*- coding: utf-8 -*-
__author__ = 'wangting'

import pika
import json
import uuid
import hashlib


class GateWatcher(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'
        ))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.conrrelation_id:
            self.response = body

    def is_authenticated(self, user_name, password):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='authenticate',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id
                                   ),
                                   body=json.dumps({'user_name': user_name, 'password': password}))
        while self.response is None:
            print(".")
            self.connection.process_data_events()
        return json.loads(self.response)['is_authenticated']


user_name = raw_input("Name: ")
password = raw_input("Password: ")
m = hashlib.md5()
m.update(password)
password = m.hexdigest()
gate_watcher = GateWatcher()
if gate_watcher.is_authenticated(user_name, password):
    amount = raw_input("How much do you want? ")
    print("Mr %s, Here your are %s" % (user_name, amount))
else:
    print("Password and username doesn't passed")

