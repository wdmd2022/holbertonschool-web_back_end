#!/usr/bin/env python3
"""this module contains a class LIFOCache which extends BaseCaching and
implements simple put and get functions using a LIFO algorithm"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """this class extends BaseCaching with basic put and get functions
    that operate on a Last-In, First-Out basis

    Args:
        BaseCaching (BaseCaching): we inherit from this class
    """

    def __init__(self):
        super().__init__()
        self.last_key_used = None

    def put(self, key, item):
        """this function assigns to the dictionary self.cache_data
        the item value for the key key. If key or item is None, the
        method does nothing. It also makes sure we have a reference to
        the first item added to the cache dictionary.

        Args:
            key (str): the key we will insert it into the dict with
            item (any): the value of the data at key location key
        """
        if (key is None or item is None):
            pass
        else:
            self.cache_data[key] = item
            previous_last_key_used = self.last_key_used
            self.last_key_used = key
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                del self.cache_data[previous_last_key_used]
                print(f"DISCARD: {previous_last_key_used}")

    def get(self, key):
        """this method returns the value in self.cache_data associated
        with the key key

        Args:
            key (str): the key we are using to search the dict with

        Returns:
            any: the value of the dictionary at key key, if it exists.
            Otherwise, returns None
        """
        if (key is None or not(key in self.cache_data)):
            return None
        return self.cache_data[key]
