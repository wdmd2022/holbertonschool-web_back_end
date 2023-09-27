#!/usr/bin/env python3
""" this module contains a class SessionAuth that inherits from Auth"""


from api.v1.auth.auth import Auth
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
