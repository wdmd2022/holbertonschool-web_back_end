#!/usr/bin/env python3
"""a simple Flask app for demonstrating i18n """


from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def welcome():
    """this basically says 'howdy' """
    return render_template(
        '0-index.html',
        title='Welcome to Holberton',
        header='Hello world'), 200


if __name__ == '__main__':
    app.run()
