#!/usr/bin/env python3
""" this module contains a class BasicAuth that extends auth"""


from api.v1.auth.auth import Auth
from models.user import User
from typing import Tuple, TypeVar
import base64


class BasicAuth(Auth):
    """ class that extends Auth to provide a different type of auth"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ returns the Base64 part of the Authorization header.
        You can assume authorization_header contains only one Basic """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ this method returns the decoded value of a Base64 string"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            llcoolvalue = base64.b64decode(base64_authorization_header)
            return llcoolvalue.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ if you like tuples you will love this method! It returns the
        user email and password from the Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        s = decoded_base64_authorization_header  # such a long name!
        colon_location = s.find(':')
        return (s[:colon_location], s[colon_location+1:])

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ this cool method returns the User instance based on email
        and password"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            search_results = User.search({'email': user_email})
        except Exception:
            return None
        for record in search_results:
            if record.is_valid_password(user_pwd):
                return record
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ overloads Auth and retrieves the User instance for a request"""
        if request is None:
            return None
        auth_header = self.authorization_header(request)
        auth_header_base_64 = self.extract_base64_authorization_header(
            auth_header)
        decoded = self.decode_base64_authorization_header(auth_header_base_64)
        emaily, passy = self.extract_user_credentials(decoded)
        return self.user_object_from_credentials(emaily, passy)
