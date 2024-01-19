from flask import Blueprint, render_template, request, redirect
from middleware.authenticator import is_valid_token
from common.util import get_username_from_jwt
from service.quiz import *


quiz_form = Blueprint("quiz_form", __name__)


@quiz_form.route('/form/quiz', methods=['GET'])
def quiz():
    token = request.cookies.get("token")
    is_valid = is_valid_token(token)
    if not is_valid:
        return redirect("/")
    username = get_username_from_jwt(token)
    data = generate_valid_question_random(username)
    user_lb_data = get_leaderboard_by(username)
    leaderboard = get_leaderboard()
    return render_template("/quiz.html",
                           quiz_data=data,
                           leaderboard=leaderboard,
                           user_lb_data=user_lb_data,
                           token_status=is_valid)

