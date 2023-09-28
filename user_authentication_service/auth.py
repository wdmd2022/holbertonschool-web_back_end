#!/usr/bin/env python3
""" file to handle auth """


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


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

    def valid_login(self, email: str, password: str) -> bool:
        """ this method uses bcrypt to check a user's password"""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(
                'utf-8'), user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ takes an email as an argument and returns the session ID
        as a string. It does this by finding the user that corresponds
        to the email, generates a new UUID and stores it in the database
        as the user's session_id, then returns that new session ID as
        a string. And it does it while only using public methods of self._db
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """takes a session id as a string and returns the user associated
        with it, unless there is none, in which case it returns None"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """destroys a session, basically logging someone out by setting
        their session_id to None. Uses only public methods of self._db"""
        self._db.update_user(user_id, session_id=None)


def _generate_uuid() -> str:
    """ this private little function generates a new uuid for us, using
    uuid4's random uuid generator"""
    return str(uuid4())


def _hash_password(password: str) -> bytes:
    """ returns the salted hash of the input password """
    na_cl = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), na_cl)
