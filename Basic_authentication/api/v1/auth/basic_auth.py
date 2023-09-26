#!/usr/bin/env python3
""" this module contains a class BasicAuth that extends auth"""


from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ class that extends Auth to provide a different type of auth"""
