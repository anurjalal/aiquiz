from flask import Blueprint, request, redirect
from service.quiz import *
from common.util import *
from webargs import fields
from webargs.flaskparser import use_args

quiz_blueprint = Blueprint("quiz", __name__)

quiz_args = {
    "question_id": fields.Int(required=True),
    "answer_id": fields.Int(required=True)
}


@quiz_blueprint.route('/save_user_answer', methods=['POST'])
@use_args(quiz_args, location="form")
def post(args):
    token = request.cookies.get("token")
    username = get_username_from_jwt(token)
    question_id = int(request.form.get('question_id'))
    answer_id = int(request.form.get('answer_id'))
    save_user_answer(username, question_id, answer_id)
    return redirect("/form/quiz")

