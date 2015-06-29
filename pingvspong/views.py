# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import time
from uuid import uuid1

from flask import current_app
from flask import render_template
from flask import request
from flask import jsonify


@current_app.route('/', methods=('GET', ))
def index():
    return render_template('index.html', uuid=uuid1().hex)


@current_app.route('/api', methods=('post', ))
def api():
    return jsonify(
        time=1
    )



