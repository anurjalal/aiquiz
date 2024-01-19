from view.backend.user import user_blueprint
from view.backend.weather import weather_blueprint
from view.backend.quiz import quiz_blueprint
from view.frontend.user_form import user_form
from view.frontend.quiz_form import quiz_form
from flask import Flask
from config.cfg import Pg
from database.sqlAlchemy import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ("{type}://{username}:{password}@{host}:{port}/{db_name}"
                                         .format(type=Pg.TYPE, username=Pg.USERNAME, password=Pg.PASSWORD,
                                                 host=Pg.HOST, port=Pg.PORT, db_name=Pg.DB_NAME))
db.init_app(app)
app.register_blueprint(user_blueprint)
app.register_blueprint(weather_blueprint)
app.register_blueprint(quiz_blueprint)
app.register_blueprint(user_form)
app.register_blueprint(quiz_form)
