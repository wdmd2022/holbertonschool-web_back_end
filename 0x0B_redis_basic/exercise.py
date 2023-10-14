#!/usr/bin/env python3
""" this module holds a cache class using redis """


import redis
from typing import Union
import uuid


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        new_key = str(uuid.uuid4())
        self._redis.set(new_key, data)
        return new_key
