# -*- coding: utf-8 -*-
try:
    from app import config_private as app_ofd_config
except ImportError:
    from app import config_publ as app_ofd_config
from datetime import datetime
import requests
from sqlalchemy.exc import IntegrityError
from flask import (
    Flask,
    request,
    jsonify,
    Response,
    json,
    redirect,
)

from app.database import db_session, init_db
from app.models import ReceiptModel, CloseshiftModel, OpenshiftModel
from app.schemas import Platformaofd

token_auth = app_ofd_config.token_auth
teleg_url = app_ofd_config.teleg_url
app = Flask(__name__)
platformaofd_schema = Platformaofd()

# Дополнительные функции
def create_response(status, request):
    status_code_dict = {
        "no_token": 400,
        "no_data": 400,
        "not_authorized": 401,
        "double": 409,
        "failed": 406,
    }
    telegram_par = {
        "chat_id": 185566253,
        "parse_mode": "Markdown",
        "text": "datetime = {}\nstatus = *{}*\njson = {}".format(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            status,
            request.json,
        ),
    }
    try:
        requests.post(
            teleg_url, telegram_par, timeout=1
        )  # Пробуем уведомить в телеграмм
    except Exception:  # Поменять
        print(
            "Telegram Failed\ndatetime = {}\nstatus = *{}*\njson = {}".format(
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                status,
                request.json,
            )
        )
    return Response(
        json.dumps({"status": status}),
        status=status_code_dict[status],
        mimetype="application/json",
    )


def try_create_new_doc(data):
    doc_type = list(data["document"].keys())[0]
    data = data["document"][doc_type]
    print(doc_type, data)
    docs_dict = {
        "receipt": {
            "Base_model": ReceiptModel,
            #"Schema": Receipt,
        },
        "openshift": {
            "Base_model": OpenshiftModel,
            #"Schema": Openshift,
        },
        "closeshift": {
            "Base_model": CloseshiftModel,
            #"Schema": Closeshift,
        },
    }
    new_doc = docs_dict[doc_type]["Base_model"]()
    for key, val in data.items():
        setattr(new_doc, key, val)
    try:
        db_session.add(new_doc)
        db_session.commit()
        result = Receipt().dump(
            ReceiptModel.query.get(new_doc.id)
        )
        return (
            jsonify(
                {
                    "status": "Created new {}".format(
                        doc_type
                    ),
                    "content": result,
                }
            ),
            201,
        )
    except IntegrityError:
        return create_response(
            status="double", request=request
        )
    except Exception as e:
        print(e)
        return create_response(
            status="failed", request=request
        )

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
def add_doc():
    if (
        "token" not in request.headers
    ):  # Если нету токена в заголовке
        return create_response(
            status="no_token", request=request
        )
    elif (
        request.headers["token"] == token_auth
    ):  # Если токен есть и он правильный
        json_input = (
            request.get_json()
        )  # Получаем JSON запроса
        if json_input is None:  # Если json пустой
            return create_response(
                status="no_data", request=request
            )
        else:  # Если json не пустой
            data = platformaofd_schema.load(
                json_input
            )  # ['document']['receipt']
            return try_create_new_doc(data)
    else:  # Если токен есть и не правильный
        return create_response(
            status="not_authorized", request=request
        )