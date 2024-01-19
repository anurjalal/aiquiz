from database.sqlAlchemy import db
from sqlalchemy.sql.expression import func


class Question(db.Model):
    __tablename__ = "question"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.String(255), unique=True)
    correct_answer_id = db.Column(db.Integer, unique=True)

    def __init__(self, question, correct_answer_id):
        self.question = question
        self.correct_answer_id = correct_answer_id


class Answer(db.Model):
    __tablename__ = "answer"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_id = db.Column(db.String(255))
    answer = db.Column(db.String(255))

    def __init__(self, question_id, answer):
        self.question_id = question_id
        self.answer = answer


class QuizResult(db.Model):
    __tablename__ = "quiz_result"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255))
    question_id_taken = db.Column(db.Integer, unique=True)
    answer_id_taken = db.Column(db.Integer)
    is_correct = db.Column(db.Boolean)

    def __init__(self, username, question_id_taken, answer_id_taken, is_correct):
        self.username = username
        self.question_id_taken = question_id_taken
        self.answer_id_taken = answer_id_taken
        self.is_correct = is_correct


class Leaderboard(db.Model):
    __tablename__ = "leaderboard"

    username = db.Column(db.String(255), primary_key=True, unique=True)
    score = db.Column(db.Integer)

    def __init__(self, username, score):
        self.username = username
        self.score = score


def generate_random_question(username):
    user_quiz_history = db.session.query(QuizResult).filter(QuizResult.username == username).all()
    question_id_taken = []
    for i in user_quiz_history:
        question_id_taken.append(i.question_id_taken)
    if len(question_id_taken) == retrieve_total_question():
        return None
    if len(question_id_taken) > 0:
        questions = db.session.query(Question).order_by(func.random()).filter(Question.id.not_in(question_id_taken))
        return questions.first()
    return db.session.query(Question).order_by(func.random()).first()


def retrieve_total_question():
    return db.session.query(Question).count()


def retrieve_answers(question_id):
    result = db.session.query(Answer).filter_by(question_id=question_id).all()
    return result


def retrieve_correct_answer(question_id):
    answer = (db.session.query(Answer).filter(Answer.question_id == question_id)
              .outerjoin(Question, Question.correct_answer_id == Answer.id).first())
    return answer


def retrieve_quiz_result(username):
    result = db.session.query(QuizResult).filter_by(username=username).all()
    return result


def insert_quiz_result(quiz_result):
    db.session.add(quiz_result)
    db.session.commit()


def retrieve_leaderboard():
    result = db.session.query(Leaderboard).order_by(Leaderboard.score.desc()).all()
    return result


def exist_in_leaderboard(username):
    exists = db.session.query(Leaderboard).filter_by(username=username).first() is not None
    return exists


def init_leaderboard(username):
    leaderboard = Leaderboard(username, 0)
    db.session.add(leaderboard)
    db.session.commit()


def update_plus_point_leaderboard(username):
    # sql alchemy lock
    user = db.session.query(Leaderboard).with_for_update().filter_by(username=username).first()
    user.score += 4
    db.session.commit()


def retrieve_leaderboard_by(username):
    leaderboard = db.session.query(Leaderboard).filter_by(username=username).first()
    return leaderboard


def is_user_taken_question(username, question_id):
    taken = db.session.query(QuizResult).filter_by(username=username, question_id_taken=question_id).first() is not None
    return taken
