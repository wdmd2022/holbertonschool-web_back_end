#!/usr/bin/env python3
""" file to handle auth """


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """takes an email and pass and makes and returns a User.
        Raises a ValueError if the user already exists"""
        try:
            new_user = self._db.find_user_by(email=email)
            if new_user:  # i.e., if it's not new but already exists
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_pass = _hash_password(password)
            confirmed_new_user = self._db.add_user(email, hashed_pass)
            return confirmed_new_user


def _hash_password(password: str) -> bytes:
    """ returns the salted hash of the input password """
    na_cl = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), na_cl)
