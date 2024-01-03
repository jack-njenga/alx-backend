#!/usr/bin/env python3
"""
Create a class BasicCache that inherits from BaseCaching
and is a caching system:
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic caching system
    """
    def __init__(self):
        """
        init
        """
        super().__init__()

    def put(self, key, item):
        """
        ...
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
