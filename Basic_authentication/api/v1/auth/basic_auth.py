#!/usr/bin/env python3
""" this module contains a class BasicAuth that extends auth"""


from api.v1.auth.auth import Auth
from typing import Tuple
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
        except base64.binascii.Error:
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
