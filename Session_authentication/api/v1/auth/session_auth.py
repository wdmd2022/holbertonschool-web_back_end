#!/usr/bin/env python3
""" this module contains a class SessionAuth that inherits from Auth"""


from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ this class lets us set up a new auth mechanism"""
