#!/usr/bin/env python3
"""this module contains a class LRUCache which extends BaseCaching and
implements simple put and get functions using a LIFO algorithm"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """this class extends BaseCaching with basic put and get functions
    that operate on a Least-Recently-Used algorithm to manage the cache size

    Args:
        BaseCaching (BaseCaching): we inherit from this class
    """

    def __init__(self):
        super().__init__()
        self.listy = []

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
            self.cache_data[key] = item  # set the value in the cache
            if key in self.listy:  # is it already in the ordered list?
                self.listy.remove(key)  # if it is, remove it
            self.listy.append(key)  # and either way, put it at the end
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                key_to_del = self.listy[-(BaseCaching.MAX_ITEMS + 1)]
                del self.cache_data[key_to_del]  # remove the LRU one
                self.listy.remove(key_to_del)
                print(f"DISCARD: {key_to_del}")

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
        if key in self.listy:  # is it already in the ordered list?
            self.listy.remove(key)  # if it is, remove it
            self.listy.append(key)  # and either way, put it at the end
        return self.cache_data[key]
