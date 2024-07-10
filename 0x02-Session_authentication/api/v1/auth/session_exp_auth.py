#!/usr/bin/env python3
""" Module of Users views
"""

from api.v1.auth.session_auth import SessionAuth
from models.user import User
import uuid
from datetime import datetime, timedelta
import os


class SessionExpAuth(SessionAuth):
    """ Session Exp Authentication
    """
    user_id_by_session_id = {}
    session_duration = 0

    def __init__(self):
        """ Init
        """
        try:
            self.session_duration = int(os.getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id: str = None) -> str:
        """ Create a session
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ User ID for Session ID
        """
        if session_id is None or session_id not in self.user_id_by_session_id:
            return None
        session_dict = self.user_id_by_session_id[session_id]
        if self.session_duration <= 0:
            return session_dict.get('user_id')
        if 'created_at' not in session_dict:
            return None
        sess_created = session_dict.get('created_at')
        time_del = timedelta(seconds=self.session_duration)
        if sess_created + time_del < datetime.now():
            return None
        return session_dict.get('user_id')
