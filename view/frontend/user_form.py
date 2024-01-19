from flask import Blueprint, render_template, request, redirect
from middleware.authenticator import is_valid_token


user_form = Blueprint("user_form", __name__)


@user_form.route('/', methods=['GET'])
def home():
    return render_template("/home.html", token_status=is_valid_token(request.cookies["token"]))


@user_form.route('/form/registration', methods=['GET'])
def registration():
    is_valid = is_valid_token(request.cookies["token"])
    if is_valid:
        return redirect("/")
    return render_template("/registration.html", token_status=is_valid)


@user_form.route('/form/login', methods=['GET'])
def login():
    is_valid = is_valid_token(request.cookies["token"])
    if is_valid:
        return redirect("/")
    return render_template("/login.html", token_status=is_valid)


