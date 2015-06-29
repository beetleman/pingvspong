# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import time
from uuid import uuid1
from functools import wraps
from datetime import datetime

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


TOKEN ='token'
CONTEST_TABLE = 'contest_table'


def check_token(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if request.form.get(TOKEN, 0, type=str) != session[TOKEN]:
            abort(403)
        return f(*args, **kwargs)
    return wrapper


def get_contest_table():
    return session.get(CONTEST_TABLE, [])


@current_app.route('/', methods=('GET', ))
def index():
    token = uuid=uuid1().hex
    session[TOKEN] = token
    session[CONTEST_TABLE] = [[0, 0]]
    return render_template('index.html', app_config={
        'token': token,
        'url': url_for('ping')
    })


@current_app.route('/api/ping', methods=('POST', ))
@check_token
def ping():
    get_contest_table().append(
        get_time(datetime.now()),
    )
    session.modified = True
    return jsonify(
        is_end=is_end(get_contest_table()),
        best_time=cal_average_diff(get_contest_table())
    )
