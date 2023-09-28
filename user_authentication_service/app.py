#!/usr/bin/env python3
""" this file initializes a flask app for us """


from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/", methods=['GET'])
def welcome():
    """this basically says 'howdy' in French"""
    return jsonify({"message": "Bienvenue"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
