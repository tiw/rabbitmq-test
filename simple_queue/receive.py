# -*- coding: utf-8 -*-
#! /usr/bin/env python

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. To exit press CTRL+C'


def callback(ch, method, properties, body):
    msg = " [x] Received %r" % (body, )
    print msg.decode('unicode-escape')

# 从名字为hello的queue里取数据
channel.basic_consume(callback, queue='hello', no_ack=True)
# 开始取
channel.start_consuming()
