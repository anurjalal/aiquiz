import jwt
from flask import request, Response
import json
from functools import wraps
from config.cfg import JWT
from http import HTTPStatus

BEARER_PREFIX = "BEARER "

# for backend
def authenticate(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]
            if auth_header.startswith(BEARER_PREFIX):
                auth_header = request.headers["Authorization"]
                token = auth_header.split()[1]
        if not token:
            message = {'message': 'cannot find token'}
            response = Response(
                json.dumps(message),
                HTTPStatus.BAD_REQUEST,
                mimetype='application/json'
            )
            return response
        try:
            jwt.decode(token, JWT.SECRET_KEY, algorithms=["HS256"])
        except:
            message = {'message': 'error decode jwt'}
            response = Response(
                json.dumps(message),
                HTTPStatus.FORBIDDEN,
                mimetype='application/json'
            )
            return response
        return f(*args, **kwargs)

    return decorator


def is_valid_token(token):
    try:
        jwt.decode(token, JWT.SECRET_KEY, algorithms=["HS256"])
    except:
        return False
    return True

