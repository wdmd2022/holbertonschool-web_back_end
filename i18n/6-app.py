#!/usr/bin/env python3
"""a simple flask app for demonstrating i18n"""


from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    return render_template('5-index.html'), 200


def get_user():
    """this checks for the user in the db (or mock db like here)"""
    try:
        return users.get(int(request.args.get('login_as')))
    except Exception:
        return None


@app.before_request
def before_request():
    """if there is a user, here is where we'll set it globally on g"""
    g.user = get_user()


if __name__ == '__main__':
    app.run()
