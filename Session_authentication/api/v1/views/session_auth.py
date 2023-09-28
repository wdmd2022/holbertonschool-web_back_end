#!/usr/bin/env python3
"""this flask view handles all routes for session authentication"""


from models.user import User
# from api.v1.views import app_views
from flask import request, jsonify
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ this lets us log in"""
    ll_cool_email = request.form.get('email')
    ll_cool_password = request.form.get('password')
    if not ll_cool_email:
        return jsonify({"error": "email missing"}), 400
    if not ll_cool_password:
        return jsonify({"error": "password missing"}), 400
    ll_cool_results = User.search({"email": ll_cool_email})
    if not ll_cool_results:
        return jsonify({"error": "no user found for this email"}), 404
    ll_cool_user = ll_cool_results[0]
    if not ll_cool_user.is_valid_password(ll_cool_password):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    ll_cool_session_id = auth.create_session(ll_cool_user.id)
    ll_cool_cookie_name = os.getenv('SESSION_NAME')
    ll_cool_user_dictionary = ll_cool_user.to_json()
    ll_cool_response = jsonify(ll_cool_user_dictionary)
    ll_cool_response.set_cookie(ll_cool_cookie_name, ll_cool_session_id)
    return ll_cool_response
