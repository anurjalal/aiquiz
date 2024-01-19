from model.quiz import *


def generate_valid_question_random(username):
    if not exist_in_leaderboard(username):
        init_leaderboard(username)
    result = {}
    question = generate_random_question(username)
    if not question:
        return result
    answer_choices = retrieve_answers(question.id)
    result["question_id"] = question.id
    result["question"] = question.question
    result["answer_choices"] = answer_choices
    return result


def is_correct(question_id, answer_id):
    answer = retrieve_correct_answer(question_id)
    return answer.id == answer_id


def update_leaderboard(username, question_id, answer_id):
    if is_correct(question_id, answer_id):
        update_plus_point_leaderboard(username)


def update_quiz_result(username, question_id, answer_id):
    correct = is_correct(question_id, answer_id)
    q = QuizResult(username, question_id, answer_id, correct)
    insert_quiz_result(q)


def save_user_answer(username, question_id, answer_id):
    if not is_user_taken_question(username, question_id):
        update_quiz_result(username, question_id, answer_id)
        update_leaderboard(username, question_id, answer_id)


def get_leaderboard():
    result = []
    leaderboard = retrieve_leaderboard()
    for i in leaderboard:
        username = i.username
        score = i.score
        result.append(dict(username=username, score=score))
    return result


def get_leaderboard_by(username):
    lb = retrieve_leaderboard_by(username)
    result = dict(username=lb.username, score=lb.score)
    return result



