#!/usr/bin/env python3
""" Auth module
"""

from flask import request
from typing import List, TypeVar
from models.user import User


class Auth:
    """ Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth
        """
        # if path is None or excluded_paths is None or excluded_paths == []:
        #     return True
        # if path[-1] != '/':
        #     path += '/'
        # if path in excluded_paths:
        #     return False
        # return True
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        for excluded_path in excluded_paths:
            if excluded_path[-1] != '/':
                excluded_path += '/'
            if excluded_path[-1] == '*' and path.startswith(excluded_path[:-1]):
                    return False
            if path == excluded_path:
                return False

    def authorization_header(self, request=None) -> str:
        """ authorization_header
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user
        """
        return None
