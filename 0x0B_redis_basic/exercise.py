#!/usr/bin/env python3
""" this module holds a cache class using redis """


import redis
from typing import Union, Optional, Callable
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwds):
        self._redis.incr(method.__qualname__)
        result = method(self, *args, **kwds)
        return result
    return wrapper


def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args):
        self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
        result = method(self, *args)
        self._redis.rpush(f"{method.__qualname__}:outputs", result)
        return result
    return wrapper


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """method to store data in our redis cache"""
        new_key = str(uuid.uuid4())
        self._redis.set(new_key, data)
        return new_key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """method to get data from redis and optionally type cast"""
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """method to parameterize get for returning strings"""
        return self.get(key, str)

    def get_int(self, key: str) -> str:
        """method to parameterize get for returning ints"""
        return self.get(key, int)
