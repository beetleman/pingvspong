# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from flask import Flask


app = Flask(__name__)
with app.app_context():
    from .views import *
