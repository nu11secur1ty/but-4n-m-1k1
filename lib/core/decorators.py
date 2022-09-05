#!/usr/bin/python
# Idea: Mauro Soria  
# Development: nu11secur1ty - 2022

import threading

from functools import wraps
from time import time

_lock = threading.Lock()
_cache = {}
_cache_lock = threading.Lock()


def cached(timeout=100):
    def _cached(func):
        @wraps(func)
        def with_caching(*args, **kwargs):
            key = id(func)
            for arg in args:
                key += id(arg)
            for k, v in kwargs:
                key += id(k) + id(v)

            # If it was cached and the cache timeout hasn't been reached
            if key in _cache and time() - _cache[key][0] < timeout:
                return _cache[key][1]

            with _cache_lock:
                result = func(*args, **kwargs)
                _cache[key] = (time(), result)

            return result

        return with_caching

    return _cached


def locked(func):
    def with_locking(*args, **kwargs):
        with _lock:
            return func(*args, **kwargs)

    return with_locking
