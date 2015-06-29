# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from flask import Flask


app = Flask(__name__)
app.secret_key = 'ksudhfoskdf23424nljknb324lknln324lnk'


with app.app_context():
    from .views import *
