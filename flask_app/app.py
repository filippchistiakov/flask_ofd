from flask_app.config import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_monitoringdashboard as dashboard
from werkzeug.contrib.fixers import ProxyFix
from flask_app.config import dash_cfg


def create_app_and_db():
    app = Flask(__name__)
    db_url = config.get("Database", "stage")
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    db = SQLAlchemy(app)
    dashboard.config.init_from(file=dash_cfg)
    dashboard.bind(app)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    return app, db

app, db = create_app_and_db()