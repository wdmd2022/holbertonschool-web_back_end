#!/usr/bin/env python3
"""this module contains a class FIFOCache which extends BaseCaching and
implements simple put and get functions using a FIFO algorithm"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """this class extends BaseCaching with basic put and get functions
    that operate on a First-In, First-Out basis

    Args:
        BaseCaching (BaseCaching): we inherit from this class
    """

    def __init__(self):
        super().__init__()

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
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                cache_key_list = list(self.cache_data)
                first_cache_key = cache_key_list[0]
                del self.cache_data[first_cache_key]
                print(f"DISCARD: {first_cache_key}")

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
