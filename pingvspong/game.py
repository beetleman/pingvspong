# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from datetime import datetime
from operator import sub, add
import time


def is_end(tab):
    return 12 == len(tab)


def get_time(dt):
    t = int(time.mktime(dt.timetuple())), dt.microsecond
    # print 'get_time', t
    return t


def time_diff(t1, t2, f=sub):
    # print 'time_diff', t1, t2
    return map(lambda x: f(*x), zip(t1, t2))


def time_diff_table(tab, f=sub):
    tab_iter = iter(tab)
    last = tab_iter.next()
    tmp = []
    for t in tab_iter:
        tmp.append(time_diff(t, last, f))
        last = t
    return tmp


def cal_average_diff(tab):
    if len(tab) < 4:
        return None
    tab = time_diff_table(tab)
    return map(lambda t: int(t/len(tab)), reduce(
        lambda acc, x: time_diff(acc, x, add),
        sorted(tab)[2:-2],  # odrzucam skrajne
        (0, 0),
    ))
