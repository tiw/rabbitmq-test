# -*- coding: utf-8 -*-
__author__ = 'wangting'

import pika
import json
import services

"""
this is a rpc server
"""

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))

channel = connection.channel()

channel.queue_declare(queue='authenticate')


def on_request(ch, method, props, body):
    req = json.loads(body)
    user_name = req['user_name']
    password = req['password']
    print(user_name, password)
    is_authenticated = services.authenticate(user_name, password)
    resp = {'is_authenticated': is_authenticated}
    print(resp)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=json.dumps(resp))
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=10)
channel.basic_consume(on_request, queue='authenticate')

channel.start_consuming()