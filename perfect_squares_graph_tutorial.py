#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
import math
from Queue import Queue

import time


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        t0 = time.time()
        res = self.bfs_optimized(n, 0)
        print(time.time() - t0)
        return res

    # def bfs(self, start, end):
    #     # start from n
    #     queue = Queue()
    #     visited = {}  # record whether a node is visited or not
    #
    #     queue.put((start, 0))
    #     visited[start] = True
    #
    #     while not queue.empty():
    #         node, step = queue.get()
    #
    #         for i in range(int(math.sqrt(node)) + 1):
    #             if node - i ** 2 == end:
    #                 return step + 1
    #
    #             if node - i ** 2 >= 0 and not visited.get(node - i**2):
    #                 queue.put((node - i**2, step + 1))
    #                 visited[node - i**2] = True

    def bfs_optimized(self, start, end):
        """
        optimized bfs
        :param start:
        :param end:
        :return:
        """
        # start from n
        queue = Queue()
        visited = {}  # record whether a node is visited or not
        # todo: Attention trick, add visit level in a (node, level) tuple
        queue.put((start, 0))
        visited[start] = True

        while not queue.empty():
            node, step = queue.get()

            # while node - i ** 2 >= 0:
            for i in range(1, int(math.sqrt(node)) + 1):
                # this is the optimize
                new_node = node - i**2
                if new_node == end:
                    return step + 1

                if new_node >= 0 and not visited.get(new_node):
                    queue.put((new_node, step + 1))
                    visited[new_node] = True


if __name__ == "__main__":
    print(Solution().numSquares(8935))
    # print(Solution().numSquares(12))

    # refer from liuyubobobo on imooc





