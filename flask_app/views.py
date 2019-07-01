# -*- coding: utf-8 -*-
from flask import (Flask, redirect, )

from flask_app.api import add_doc
from flask_app.database import db_session, init_db

app = Flask(__name__)


# Дополнительные функции
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.before_first_request
def init_db_first():
    init_db()


@app.route("/", methods=["GET"])
def index():
    return redirect("/dash", code=302)


@app.route(
    "/acceptreceipt/platformaofd/", methods=["GET", "POST"]
)
def get_webhook():
    return add_doc()
