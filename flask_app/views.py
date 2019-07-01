# -*- coding: utf-8 -*-
from flask import  redirect
from flask_app.api import add_doc
from flask_app.app import app, db

# Дополнительные функции
@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


@app.before_first_request
def init_request():
    db.create_all()


@app.route("/", methods=["GET"])
def index():
    return redirect("/dash", code=302)


@app.route(
    "/acceptreceipt/platformaofd/", methods=["GET", "POST"]
)
def get_webhook():
    return add_doc()
