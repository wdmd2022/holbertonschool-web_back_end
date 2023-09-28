#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None


if os.environ.get('AUTH_TYPE') == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()
if os.environ.get('AUTH_TYPE') == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
if os.environ.get('AUTH_TYPE') == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Not authorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


"""@app.before_request
def before_request():
    """  # filters each request to see if auth is needed
"""
    paths_to_check = ['/api/v1/status/', 'api/v1/unauthorized/',
                      'api/v1/forbidden/', 'api/v1/auth_session/login/']
    try:
        app.url_map.bind('localhost').match(request.path)
    except BuildError:
        abort(404)
    if auth is None:
        return
    if not auth.require_auth(request.path, paths_to_check):
        return
    if auth.current_user(request) is None:
        abort(403)
    if auth.authorization_header(request) is None and auth.session_cookie(
                                                request) is None:
        abort(401)
    if auth.authorization_header(request) is None:
        abort(401)
    request.current_user = auth.current_user(request)"""


@app.before_request
def before_request():
    """ filters each request to see if auth is needed"""
    paths_to_check = ['/api/v1/status/', '/api/v1/unauthorized/',
                      '/api/v1/forbidden/', '/api/v1/auth_session/login/']
    if request.endpoint is None:
        abort(404)
    if auth is None:
        return
    if not auth.require_auth(request.path, paths_to_check):
        return
    if auth.authorization_header(request) is None and auth.session_cookie(
                                                            request) is None:
        abort(401)
    if auth.current_user(request) is None:
        if (auth.authorization_header(request) is not None
           or auth.session_cookie(request) is not None):
            abort(403)
    request.current_user = auth.current_user(request)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
