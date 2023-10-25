#!/usr/bin/env python3
"""A caching system"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''Inherits from baseCaching'''

    def __init__(self):
        '''initializes the class'''
        BaseCaching.__init__(self)

    def put(self, key, item):
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
