import jwt


def get_username_from_jwt(token):
    decoded = jwt.decode(token, options={"verify_signature": False})
    return decoded["username"]
