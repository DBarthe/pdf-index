# -*- coding: utf-8 -*-

from itertools import takewhile, dropwhile


def debug(token):
    print token
    return token


def lowercase(token):
    return token.lower()


def trim_special_chars(token):
    def aux(t):
        return "".join(takewhile(lambda c: c.isalpha(), dropwhile(lambda c: not c.isalpha(), t)))
    new_token = aux(token)
    if len(new_token) == 0:
        return []
    elif new_token == token:
        return [ new_token ]
    else:
        tokens = trim_special_chars(token[:len(new_token)])
        tokens.append(new_token)
        return tokens


def min_length(min):
    def f(token):
        return token if len(token) >= min else None
    return f