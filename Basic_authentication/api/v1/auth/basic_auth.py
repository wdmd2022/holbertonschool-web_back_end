#!/usr/bin/env python3
""" this module contains a class BasicAuth that extends auth"""


from api.v1.auth.auth import Auth


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
