#!/usr/bin/env python

import hashlib


secret_book = {
    'ting': 'test1234',
    'jack': 'priate',
    'mobi': 'seefood'
}

count = 0


def authenticate(user_name, password):
    """
    This function simulate a service for authenticate user
    """
    global count
    count = count + 1
    print count
    if user_name not in secret_book.keys():
        return False

    m = hashlib.md5()
    m.update(secret_book[user_name])
    return password == m.hexdigest()


if __name__ == '__main__':

    if not authenticate('ting', '16d7a4fca7442dda3ad93c9a726597e4'):
        print "too bad"
    else:
        print "cool!"

    print authenticate('nobody', 'what ever')
