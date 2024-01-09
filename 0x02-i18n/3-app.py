#!/usr/bin/env python3
"""
parametrizing templates
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    configs
    """
    LANGUAGES = ["en", "fr"]
    LOCALE = "en"
    TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    locale
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", strict_slashes=False)
def homapage():
    """
    homepage
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
