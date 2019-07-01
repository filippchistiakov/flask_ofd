from datetime import datetime

import requests
from flask import (
    request,
    jsonify,
    Response,
    json,
)
from sqlalchemy.exc import IntegrityError

from flask_app.config import config
from flask_app.database import db_session
from flask_app.models import ReceiptModel, CloseshiftModel, OpenshiftModel
from flask_app.schemas import Platformaofd

token_auth = config.get("Authentication", "token")
teleg_url = config.get("Telegram", "url")
platformaofd_schema = Platformaofd()


# Ф-ция создания ответа и уведомления в телеграмм
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


# Ф-ция которая отправляет данные в БД, data - это валидированный json
def try_create_new_doc(data):
    doc_type = list(data["document"].keys())[0]
    data = data["document"][doc_type]
    print(doc_type, data)
    docs_dict = {
        "receipt": {
            "Base_model": ReceiptModel,
            # "Schema": Receipt,
        },
        "openshift": {
            "Base_model": OpenshiftModel,
            # "Schema": Openshift,
        },
        "closeshift": {
            "Base_model": CloseshiftModel,
            # "Schema": Closeshift,
        },
    }
    new_doc = docs_dict[doc_type]["Base_model"]()
    for key, val in data.items():
        setattr(new_doc, key, val)
    try:
        db_session.add(new_doc)
        db_session.commit()
        return (
            jsonify(
                {
                    "status": "Created new {}".format(
                        doc_type
                    ),
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


# Ф-ция которая получает хук валидирует json и вызывает create_response и try_create_new_doc
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
