#!/usr/bine/env python3


"""
A simple module to learn the basics
of working with redis and redis python
client
"""

from redis import Redis
from typing import Union
from uuid import uuid4

param_type = Union[str, bytes, int, float]


class Cache:
    """
    A simple class to for caching
    Using redis server
    """

    def __init__(self):
        """The default constructor"""
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: param_type) -> str:
        """
        Store the data in redis server
        Args:
            data (Union[str, bytes, int or float.])
        Returns:
            Returns a string
        """
        self.random_key = str(uuid4())
        self._redis.set(self.random_key, data)
        return self.random_key
