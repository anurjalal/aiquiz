from model.user import User, insert_user, retrieve_user_by_username
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from config.cfg import JWT
import jwt
from common.response import CommonResponse


def save_user(username, password):
    password_hash = generate_password_hash(password)
    user_exist = retrieve_user_by_username(username=username) is not None
    if user_exist:
        return CommonResponse(False, "username sudah digunakan, silahkan gunakan username yang lain")
    new_user = User(
        username=username,
        password=password_hash
    )
    insert_user(new_user)
    return CommonResponse(True, "Registrasi Berhasil")


def generate_token(username, password):
    user = retrieve_user_by_username(username)
    if user is not None:
        if check_password_hash(user.password, password):
            token = jwt.encode(
                {'username': username, 'exp': datetime.utcnow() + timedelta(minutes=JWT.EXPIRATION_MINUTE)},
                JWT.SECRET_KEY, "HS256")
            return token
    return ""

