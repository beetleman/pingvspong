# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from datetime import (
    datetime,
)
from operator import sub, add
import time


def is_end(tab):
    return 12 == len(tab)


def get_time(dt, offset=None):
    return  int(time.mktime(dt.timetuple())) , dt.microsecond
    return time_diff(t, offset or (0, 0), f=sub)


def time_diff(t1, t2, f=sub):
    # print 'time_diff', t1, t2
    diff = map(lambda x: f(*x), zip(t1, t2))
    if diff[1] < 0:
        return diff[0] - 1, 1000000 + diff[1]
    return diff


def cal_average_diff(tab):
    if len(tab) < 5:
        return None
    tab = sorted(tab)[2:-2]  # odrzucam skrajne
    return map(lambda t: int(t / len(tab)), reduce(
        lambda acc, x: time_diff(acc, x, add),
        tab,
        (0, 0),
    ))
