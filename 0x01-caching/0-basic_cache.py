#!/usr/bin/env python3
"""Basic Dict"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """basiccache inherits from the basecatching"""

    def put(self, key, item):
        """updating cache in the dict"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """returns value at a certain key"""
        if key is None:
            return None
        return self.cache_data.get(key)
