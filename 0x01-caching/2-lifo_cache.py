#!/usr/bin/env python3
"""
Create a class LIFOCache that inherits from BaseCaching and
is a caching system:
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO Caching System
    """
    def __init__(self):
        """
        init
        """
        super().__init__()
        self._lifo = []

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    discarded = self.cache_data.popitem()[0]
                    print(f"DISCARD: {discarded}")
            else:
                del self.cache_data[key]
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
