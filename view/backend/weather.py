from flask import Blueprint, request, render_template
from middleware.authenticator import is_valid_token
from service import weather
from webargs import fields
from webargs.flaskparser import use_args

weather_blueprint = Blueprint("weather", __name__)

weatherapi_args = {"location": fields.Str(validate=lambda p: 0 < len(p) <= 255),}


@weather_blueprint.route('/weather_3day', methods=['GET'])
@use_args(weatherapi_args, location="form")
def get_weather_3day(args):
    location = request.args.get('location')
    forcast = weather.get_3day_forecast(location)
    return render_template("home.html",
                           location=location,
                           forcast=forcast,
                           token_status=is_valid_token(request.cookies.get("token")))
