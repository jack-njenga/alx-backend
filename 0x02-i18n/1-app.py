#!/usr/bin/env python3
"""
Basic Babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    basic configs
    """
    LANGUAGES = ["en", "fr"]
    LOCALE = "en"
    TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
Babel = Babel(app)


@app.route("/", strict_slashes=False)
def index():
    """
    homepage
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
