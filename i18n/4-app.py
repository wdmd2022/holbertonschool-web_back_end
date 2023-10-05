#!/usr/bin/env python3
"""a simple flask app for demonstrating i18n"""


from flask import Flask, render_template, request
from flask_babel import Babel, _  # pylint: disable=missing-function-docstring


class Config():
    """we configure our Babel languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """grabs the lcoale when a request is made"""
    url_locale = request.args.get('locale')
    if url_locale and url_locale in Config.LANGUAGES:
        return url_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=['GET'], strict_slashes=False)
def welcome():
    """this basically says 'howdy' """
    return render_template('4-index.html'), 200


if __name__ == '__main__':
    app.run()
