# -*- coding: utf-8 -*-

import collections


def flatten(l):
    for el in l:
        if isinstance(el, collections.abc.Iterable) and not isinstance(el, str):
            for sub in flatten(el):
                yield sub
        else:
            yield el
