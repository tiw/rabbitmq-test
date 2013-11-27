# -*- coding: utf-8 -*-
#! /usr/bin/env python

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

# 建立一个名字叫做hello的队列
channel.queue_declare(queue='hello')

# exchange是必须的
# routing_key对应队列的名字
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=u'Hello World! 王挺')
print '[x] Sent \'Hello World!\''
connection.close()
