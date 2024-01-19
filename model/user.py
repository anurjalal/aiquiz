from database.sqlAlchemy import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, username, password):
        self.username = username
        self.password = password


def insert_user(user):
    db.session.add(user)
    db.session.commit()


def retrieve_user_by_username(username):
    result = db.session.query(User).filter_by(username=username).first()
    return result

