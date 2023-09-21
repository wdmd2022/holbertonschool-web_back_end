#!/usr/bin/env python3
"""
salts and returns your password to you after hashing it
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """
    turns your ordinary password into a salty, hashy bytestring
    """
    codey_p = password.encode('utf-8')
    return (bcrypt.hashpw(codey_p, bcrypt.gensalt()))


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Yep, that looks like a hashed password
    """
    codey_p = password.encode('utf-8')
    if bcrypt.checkpw(codey_p, hashed_password):
        return True
    return False
