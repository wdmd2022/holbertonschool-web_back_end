#!/usr/bin/env python3
""" this module contains a class SessionAuth that inherits from Auth"""


from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """ this class lets us set up a new auth mechanism"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """this method creates a session ID for a user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ returns a User ID based on a session ID, which is pretty cool """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """returns a User instance based on a cookie value"""
        if request is None:
            return None
        cool_session_id = self.session_cookie(request)
        if cool_session_id is None:
            return None
        cool_user_id = self.user_id_for_session_id(cool_session_id)
        if cool_user_id is None:
            return None
        cool_user = User.get(cool_user_id)
        return cool_user
