#!/usr/bin/env python3
"""Auth module.
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """ implements the hash_password function
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
