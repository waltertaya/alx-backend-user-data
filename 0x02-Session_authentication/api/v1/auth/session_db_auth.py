#!/usr/bin/env python3
""" Module of Users views
"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
import uuid
from datetime import datetime
import os


class SessionDBAuth(SessionExpAuth):
    """ Session DB Authentication
    """
    def create_session(self, user_id: str = None) -> str:
        """ Create a session
        """
        if user_id is None or type(user_id) is not str:
            return None
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ User ID for Session ID
        """
        if session_id is None or type(session_id) is not str:
            return None
        user_sessions = UserSession.search({'session_id': session_id})
        if not user_sessions:
            return None
        user_session = user_sessions[0]
        if self.session_duration <= 0:
            return user_session.user_id
        if 'created_at' not in user_session:
            return None
        sess_created = user_session.created_at
        if sess_created + self.session_duration < datetime.now():
            return None
        return user_session.user_id

    def destroy_session(self, request=None):
        """ destroy_session
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_sessions = UserSession.search({'session_id': session_id})
        if not user_sessions:
            return False
        user_session = user_sessions[0]
        user_session.remove()
        return True
