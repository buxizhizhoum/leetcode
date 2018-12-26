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
from collections import deque


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.queue = deque([])
        self.size = 0
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        self.queue.remove(key)
        self.queue.append(key)
        return self.cache.get(key)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.cache:
            self.cache[key] = value
            self.queue.append(key)
            self.size += 1

            # check size
            if self.size > self.capacity:
                expire_key = self.queue.popleft()
                self.cache.pop(expire_key)
                self.size -= 1
        else:
            self.cache[key] = value
            # get this key and put it to end of queue
            self.queue.remove(key)
            self.queue.append(key)


if __name__ == "__main__":
    # Your LRUCache object will be instantiated and called as such:
    obj = LRUCache(10)
    for i in range(100):
        obj.put(i, i)
    for i in range(100):
        param_1 = obj.get(i)
        print(param_1)



