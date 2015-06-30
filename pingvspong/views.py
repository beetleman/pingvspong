# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import time
from uuid import uuid1
from functools import wraps
from datetime import datetime
from operator import add

from flask import (
    current_app,
    render_template,
    request,
    session,
    jsonify,
    abort,
    url_for
)

from .game import (
    is_end,
    cal_average_diff,
    time_diff,
    get_time
)


TOKEN = 'token'
CONTEST_TABLE = 'contest_table'
LAST_TIME = 'last_time'
PAUSE_TIME = (0, 700000)

def check_token(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if request.form.get(TOKEN, 0, type=str) != session[TOKEN]:
            abort(403)
        return f(*args, **kwargs)
    return wrapper


def get_contest_table():
    return session.get(CONTEST_TABLE, [])


def get_last_time():
    return session.get(LAST_TIME, None)


def set_last_time(t):
    session[LAST_TIME] = time_diff(
        t,
        PAUSE_TIME,
        add
    )


@current_app.route('/', methods=('GET', ))
def index():
    token = uuid = uuid1().hex
    session[TOKEN] = token
    session[CONTEST_TABLE] = []
    set_last_time(get_time(datetime.now()))
    return render_template('index.html', app_config={
        'token': token,
        'url': url_for('ping'),
        'pause_time': PAUSE_TIME[0]*1000 + PAUSE_TIME[1]/1000.0
    })


@current_app.route('/api/ping', methods=('POST', ))
@check_token
def ping():
    dt = datetime.now()
    current_time = get_time(dt)

    if get_last_time() is not None:
        current_time_diff = time_diff(
            current_time,
            get_last_time()
        )
    else:
        current_time_diff = None

    get_contest_table().append(
        current_time_diff,
    )
    set_last_time(current_time)
    session.modified = True

    return jsonify(
        is_end=is_end(get_contest_table()),
        average_time=cal_average_diff(get_contest_table()),
        last_time=current_time_diff
    )
