#!/usr/bin/env python3
""" this module holds a cache class using redis """


import redis
from typing import Union, Optional, Callable
import uuid


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        new_key = str(uuid.uuid4())
        self._redis.set(new_key, data)
        return new_key

    def get(self,
            key: str,
            fn: Optional[Callable]) -> Union[str, bytes, int, float]:
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        return self.get(key, str)

    def get_int(self, key: str) -> str:
        return self.get(key, int)
