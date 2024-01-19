from flask import Blueprint, request, render_template
from middleware.authenticator import is_valid_token
from service import weather

weather_blueprint = Blueprint("weather", __name__)


@weather_blueprint.route('/weather_3day', methods=['GET'])
def get_weather_3day():
    location = request.args.get('location')
    forcast = weather.get_3day_forecast(location)
    return render_template("home.html",
                           location=location,
                           forcast=forcast,
                           token_status=is_valid_token(request.cookies.get("token")))
