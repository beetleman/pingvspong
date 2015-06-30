# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from operator import sub, add
import time
from functools import (
    reduce,
    wraps
)


def tuplefity(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        r = f(*args, **kwargs)
        if r is not None:
            return tuple(r)
        return r
    return wrapper


def is_end(tab):
    return 12 == len(tab)


def get_time(dt, offset=None):
    return int(time.mktime(dt.timetuple())), dt.microsecond


def time_diff(t1, t2, f=sub):
    diff = tuple(map(lambda x: f(*x), zip(t1, t2)))
    if diff[1] < 0:
        return diff[0] - 1, 1000000 + diff[1]
    return diff


@tuplefity
def cal_average_diff(tab):
    if len(tab) < 5:
        return None
    tab = tuple(sorted(tab))[2:-2]  # odrzucam skrajne
    return map(lambda t: int(t / len(tab)), reduce(
        lambda acc, x: time_diff(acc, x, add),
        tab,
        (0, 0),
    ))
