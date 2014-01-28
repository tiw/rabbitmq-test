# -*- coding: utf-8 -*-
__author__ = 'wangting'

import requests
import hashlib


def authenticate():
    name = raw_input("Enter your name:")
    password = raw_input("Enter your password:")

    md5 = hashlib.md5()
    md5.update(password)
    secret = md5.hexdigest()
    r = requests.post('http://127.0.0.1:5000/authenticate', {'user_name': name, 'password': secret})
    return r.json()[u'is_authenticated']


def give_me_money():
    if not authenticate():
        print "Wrong name or password"
    else:
        amount = raw_input("How much do you want?")
        print "Here you are, %s" % amount


if __name__ == '__main__':
    for i in range(1, 1000):
        name = 'foo'
        secret = 'bar'
        r = requests.post('http://127.0.0.1:5000/authenticate', {'user_name': name, 'password': secret})
    give_me_money()

