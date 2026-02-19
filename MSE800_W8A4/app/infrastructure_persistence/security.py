"""
SECURITY helpers
hash password here only, no import from db_manager.
"""

import hashlib


def hash_password(password: str) -> str:
    # turn password into sha256 so not saving plain text
    return hashlib.sha256(password.encode("utf-8")).hexdigest()
