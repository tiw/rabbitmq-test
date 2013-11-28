# -*- coding: utf-8 -*-
__author__ = 'wangting'
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))


