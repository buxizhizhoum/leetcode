#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.
"""


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        # cache = [float("-inf") for _ in range(n+1)]  # 0 to n
        # return self.recursion_version(n, cache)
        return self.dynamic_programming(n)

    def recursion_version(self, n, cache):
        if n == 1:
            return 1

        if cache[n] != float("-inf"):
            return cache[n]

        res = float("-inf")
        for i in range(1, n):
            res = max(res, i * (n - i), i * self.recursion_version(n-i, cache))
            cache[n] = res
        return res

    @staticmethod
    def dynamic_programming(n):
        cache = [float("-inf") for _ in range(0, n+1)]

        cache[1] = 1

        for i in range(2, n+1):
            res = -1
            # this loop to calculate f(i)
            for j in range(1, i):
                # (i-j) * cache[j] is function part
                res = max(res, j*(i-j), (i-j) * cache[j])
            cache[i] = res
        return cache[n]


if __name__ == "__main__":
    print(Solution().integerBreak(10))






