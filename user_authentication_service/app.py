#!/usr/bin/env python3
""" this file initializes a flask app for us """


from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth


AUTH = Auth()

app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def welcome():
    """this basically says 'howdy' in French"""
    return jsonify({"message": "Bienvenue"}), 200


@app.route("/users", methods=['POST'], strict_slashes=False)
def users():
    """this is the endpoint to register a user"""
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        new_user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login():
    """ this is where we implement a login function to respond to the route"""
    email = request.form.get("email")
    password = request.form.get("password")
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    resp = make_response(jsonify({"email": email, "message": "logged in"}))
    resp.set_cookie("session_id", session_id)
    return resp


@app.route("/sessions", methods=['DELETE'], strict_slashes=False)
def logout():
    """this is where we log the user out by setting their sessiont to None"""
    session_id = request.cookies.get("session_id")  # it's in the cookie
    user = AUTH.get_user_from_session_id(session_id)  # now we get the user
    if user:
        AUTH.destroy_session(user.id)
        return redirect("/")
    else:
        abort(403)


@app.route("/profile", methods=['GET'], strict_slashes=False)
def profile():
    """ this is where we implement a profile function to respond
    to the route. Like with logout, we expect the request to contain
    a session_id cookie."""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


@app.route("/reset_password", methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """this is where we generate the reset password token"""
    email = request.form.get("email")  # I sure like form data
    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except ValueError:
        abort(403)


@app.route("/reset_password", methods=['PUT'], strict_slashes=False)
def update_password():
    """this endpoint lets us actually reset the password"""
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")
    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
