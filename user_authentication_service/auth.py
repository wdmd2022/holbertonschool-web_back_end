#!/usr/bin/env python3
""" file to handle auth """


import bcrypt


def _hash_password(password: str) -> bytes:
    """ returns the salted hash of the input password """
    na_cl = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), na_cl)
