#!/usr/bin/env python3
"""this module contains a class that manages API authentication"""


from flask import request
from typing import List, TypeVar


class Auth:
    """ class created to manage API authentication
    """
    def __init__(self):
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ this public method returns False if auth is required
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        if not path.endswith('/'):
            path = path + '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ this public method returns None; later, though, we will see
        that request will be the Flask request object"""
        if request is None:
            return None
        return request.headers.get('Authorization')  # returns None if !exist

    def current_user(self, request=None) -> TypeVar('User'):
        """ this public method returns None; later, though, we will see
        that request will be the Flask request object"""
        return None
