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


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = [-1 for _ in range(n+1)]
        # return self.recursion(n)
        # return self.recursion_cache(n, cache)
        return self.dynamic_programming(n)

    def recursion(self, n):
        # if a number is already perfect squares, stop recursion.
        if int(math.sqrt(n)) ** 2 == n:
            return 1

        res = float("inf")
        square_up_limit = int(math.ceil(math.sqrt(n)))
        for i in range(1, square_up_limit):
            square = i ** 2
            if square <= n:
                res = min(res, 1 + self.recursion(n - square))
        return res

    def recursion_cache(self, n, cache):
        # if a number is already perfect squares, stop recursion.
        if int(math.sqrt(n)) ** 2 == n:
            return 1

        if cache[n] != -1:
            return cache[n]

        res = float("inf")
        square_up_limit = int(math.ceil(math.sqrt(n)))
        for i in range(1, square_up_limit+1):
            square = i ** 2
            if square <= n:
                res = min(res, 1 + self.recursion_cache(n - square, cache))
        cache[n] = res
        return cache[n]

    @staticmethod
    def dynamic_programming(n):
        cache = [-1 for _ in range(n+1)]

        # initialize cache
        square_up_limit = int(math.ceil(math.sqrt(n)))
        for i in range(1, square_up_limit+1):
            if i**2 <= n:
                cache[i**2] = 1
        cache[0] = 0
        cache[1] = 1

        if cache[n] != -1:
            return cache[n]

        for i in range(2, n+1):
            # todo: Attention res initialization here, compare with recursion
            res = float("inf")
            for j in range(1, i//2 + 1):
                if i != j**2:
                    res_tmp = cache[j] + cache[i - j]
                    res = min(res, res_tmp)
                else:
                    # if i is perfect square, it is initialized in cache
                    res = cache[i]
            # todo: Attention the different place to update cache
            cache[i] = res
        return cache[n]


if __name__ == "__main__":
    print(Solution().numSquares(7168))



