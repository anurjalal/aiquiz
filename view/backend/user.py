from flask import Blueprint, request, make_response, render_template, redirect
from service import user
from common.response import CommonResponse
from middleware.authenticator import is_valid_token
from webargs import fields
from webargs.flaskparser import use_args

user_blueprint = Blueprint("user", __name__)

login_args = {
    "username": fields.Str(validate=lambda p: 0 < len(p) <= 255),
    "password": fields.Str(validate=lambda p: 0 < len(p) <= 255),
}

signup_args = (login_args |
               {"password_confirmation": fields.Str(validate=lambda p: 0 < len(p) <= 255)})

@user_blueprint.route('/signup', methods=['POST'])
@use_args(signup_args, location="form")
def signup(args):
    is_valid = is_valid_token(request.cookies.get("token"))
    if is_valid:
        return redirect("/")
    username = request.form.get('username')
    password = request.form.get('password')
    password_confirmation = request.form.get('password_confirmation')
    if password != password_confirmation:
        result = CommonResponse(False, "konfirmasi password tidak cocok")
    else:
        result = user.save_user(username, password)
    return render_template("registration.html", response=result, token_status=is_valid)


@user_blueprint.route('/login', methods=['POST'])
@use_args(login_args, location="form")
def login(args):
    is_valid = is_valid_token(request.cookies.get("token"))
    if is_valid:
        return redirect("/")
    username = request.form.get('username')
    password = request.form.get('password')
    token = user.generate_token(username, password)
    if token:
        response = CommonResponse(True, "Login Berhasil")
        is_valid = True
    else:
        response = CommonResponse(False, "Login Gagal")
    result = make_response(render_template('home.html', response=response, token_status=is_valid))
    result.set_cookie('token', token)
    return result


@user_blueprint.route('/logout', methods=['GET'])
def logout():
    response = CommonResponse(True, "Berhasil Logout")
    result = make_response(render_template('home.html', response=response, token_status=False))
    result.set_cookie('token', "")
    return result

