#!/usr/bin/env python3
"""
user login system emulation
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


class Config:
    """
    configs
    """
    LANGUAGES = ["en", "fr"]
    LOCALE = "en"
    TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    locale
    """
    locale = request.args.get('locale')
    if locale:
        if locale in app.config["LANGUAGES"]:
            return locale
    elif g.user:
        locale = g.user.get('locale')
        if locale in app.config["LANGUAGES"]:
            return locale
    elif request.accept_languages:
        return request.accept_languages.best_match(app.config["LANGUAGES"])
    return app.config["LOCALE"]


@babel.timezoneselector
def get_timezone() -> str:
    """
    Timezone
    """
    timezone = request.args.get("timezone", "").split()
    if not timezone and g.user:
        timezone = g.user.get("timezone")
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config["TIMEZONE"]


def get_user():
    """
    returns user
    """
    login_id = request.args.get("login_as")
    if login_id:
        return users.get(int(login_id), None)
    return None


@app.route("/", strict_slashes=False)
def homepage():
    """
    homepage
    """
    return render_template("7-index.html")


@app.before_request
def before_request():
    """
    starting point
    """
    user = get_user()
    g.user = user


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
