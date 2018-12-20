#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        cache = {}
        cache[0] = 1
        cache[1] = x
        # return self.recursion(x, n, cache)
        # return self.backtracking(x, n)
        return self.ans(x, n, cache)

    def ans(self, x, n, cache):
        res = self._ans(x, abs(n), cache)
        if n < 0:
            return 1.0 / res
        return res

    def _ans(self, x, n, cache):
        if n == 0:
            return cache[0]
        if n == 1:
            return x

        new_n = n // 2
        rest = n % 2

        tmp_res = self._ans(x, new_n, cache)
        res = tmp_res * tmp_res * self._ans(x, rest, cache)
        cache[n] = res
        return res

    def recursion(self, x, n, cache):
        res = self._recursion(x, abs(n), cache)
        if n < 0:
            return 1.0 / res
        return res

    def _recursion(self, x, n, cache):
        if n == 0:
            cache[0] = 1
            return x

        if cache.get(n-1) is not None:
            return cache[n-1] * x
        else:
            cache[n] = x * self._recursion(x, n-1, cache)
            return cache[n]

    def _backtracking(self, x, n, cache):
        for i in range(1, n+1):
            cache[i] = cache[i-1] * x

        return cache[n]

    def _backtracking_1(self, x, n):
        tmp = 1
        for i in xrange(1, n+1):
            tmp *= x

        return tmp

    def backtracking(self, x, n):
        # res = self._backtracking(x, abs(n), cache)
        res = self._backtracking_1(x, abs(n))
        if n < 0:
            return 1.0 / res
        return res

if __name__ == "__main__":
    print(Solution().myPow(2, -10))
    print(Solution().myPow(0.44528, 0))
    print(Solution().myPow(1.00001, 123456))
    print(Solution().myPow(0.00001, 2147483647))
    print(Solution().myPow(1.000000001, 2147483647))


