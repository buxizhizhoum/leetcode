#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache,
otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
from collections import OrderedDict


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        # move key, value to end of ordered dict
        value = self.cache.get(key)
        # pop it and add again to ensure it is at the end of ordered dict
        self.cache.pop(key)
        self.cache[key] = value
        return self.cache.get(key)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.cache:
            self.cache[key] = value

            # check size
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)
        else:
            # pop this key and put it to end of ordered dict
            self.cache.pop(key)
            # this is update value
            self.cache[key] = value


if __name__ == "__main__":
    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(10)
    # for i in range(100):
    #     obj.put(i, i)
    # for i in range(100):
    #     param_1 = obj.get(i)
    #     print(param_1)

    obj = LRUCache(2)
    operations = ["put", "put", "get", "put", "get", "put", "get", "get", "get"]
    parameters = [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    for operation, param in zip(operations, parameters):
        if hasattr(obj, operation):
            method = getattr(obj, operation)
            print(method(*param))

    # ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    # [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]



