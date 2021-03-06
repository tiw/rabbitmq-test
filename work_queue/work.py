# -*- coding: utf-8 -*-
__author__ = 'wangting'

# Worker does the job

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print " [*] Waiting for message. To exit press CTRL+C"


def callback(ch, method, properties, body):
    print " [x] Received % r", (body,)
    time.sleep(body.count('..'))
    print " [x] Done"
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)


# subscribe 用的是basic_consume
channel.basic_consume(callback, queue='task_queue')

channel.start_consuming()