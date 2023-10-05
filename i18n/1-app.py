#!/usr/bin/env python3
"""a simple flask app for demonstrating i18n"""


from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """we configure our Babel languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/", methods=['GET'], strict_slashes=False)
def welcome():
    """this basically says 'howdy' """
    return render_template('1-index.html'), 200


if __name__ == '__main__':
    app.run()
