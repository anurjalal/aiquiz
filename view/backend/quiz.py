from flask import Blueprint, request, redirect
from service.quiz import *
from common.util import *

quiz_blueprint = Blueprint("quiz", __name__)


@quiz_blueprint.route('/save_user_answer', methods=['POST'])
def post():
    token = request.cookies["token"]
    username = get_username_from_jwt(token)
    question_id = int(request.form.get('question_id'))
    answer_id = int(request.form.get('answer_id'))
    save_user_answer(username, question_id, answer_id)
    return redirect("/form/quiz")

