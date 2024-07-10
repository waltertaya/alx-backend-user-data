#!/usr/bin/env python3
""" Auth module
    Class BasicAuth that inherits from Auth
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ extract_base64_authorization_header
        """
        type_check = type(authorization_header)
        if authorization_header is None or type_check is not str:
            return None
        if authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ decode_base64_authorization_header
        """
        import base64
        type_check = type(base64_authorization_header)
        if base64_authorization_header is None or type_check is not str:
            return None
        try:
            base64_bytes = base64_authorization_header.encode('utf-8')
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('utf-8')
            return message
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ extract_user_credentials
        """
        type_check = type(decoded_base64_authorization_header)
        base64_decoded = decoded_base64_authorization_header
        if base64_decoded is None or type_check is not str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        user_credentials = base64_decoded.split(':', 1)
        return user_credentials[0], user_credentials[1]

    def user_object_from_credentials(self, user_email: str, user_pwd: str
                                     ) -> Auth:
        """ user_object_from_credentials
        """
        if user_email is None or user_pwd is None:
            return None
        try:
            user = Auth()
            user.email = user_email
            user.password = user_pwd
            return user
        except Exception:
            return None