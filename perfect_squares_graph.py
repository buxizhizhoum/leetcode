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
        graph = self.create_graph(n)
        t1 = time.time()
        print(t1 - t0)
        res = self.bfs(graph, n, 0)
        print(time.time() - t1)
        return res

    def create_graph(self, n):
        # todo: think directed or not directed?
        # directed, current node point to nodes that are less than current node
        graph = {i: [] for i in range(n+1)}

        for i in range(n+1):
            # node connected to a old node should be less than old node
            for j in range(i):
                # if i != j and i diff j with one square number
                if self.is_square(i-j):
                    graph[i].append(j)

        return graph

    @staticmethod
    def is_square(number):
        """
        check whether a number is a square of some number
        :param number:
        :return:
        """
        if int(math.sqrt(number))**2 == number:
            return True
        return False

    def bfs(self, graph, start, end):
        # start from n
        queue = Queue()
        visited = {}  # record whether a node is visited or not
        order = {}  # record visit order of a node

        queue.put(start)
        visited[start] = True
        order[start] = 0

        while not queue.empty():
            node = queue.get()
            # if node == end:
            #     return order[node]
            # get next level nodes
            neighbors = graph[node]
            for new_node in neighbors:
                # if new_node diff node with one square number, put to queue
                if not visited.get(new_node) and self.is_square(abs(node - new_node)):
                    queue.put(new_node)
                    visited[new_node] = True
                    order[new_node] = order[node] + 1

        return order.get(end)


if __name__ == "__main__":
    print(Solution().numSquares(7000))

    # time limit exceeded



