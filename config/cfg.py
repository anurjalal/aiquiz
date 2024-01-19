import os


class Pg:
    TYPE = os.getenv("DB_TYPE")
    HOST = os.getenv("DB_HOST")
    USERNAME = os.getenv("DB_USERNAME")
    PASSWORD = os.getenv("DB_PASSWORD")
    PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")


class JWT:
    SECRET_KEY = os.getenv("SECRET_KEY")
    EXPIRATION_MINUTE = 45
