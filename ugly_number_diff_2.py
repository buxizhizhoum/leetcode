#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.
"""


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.ans(n)

    def ans(self, n):
        res = [1]
        p2, p3, p5 = 0, 0, 0

        i = 1  # res len == n, res initialized with [1]
        while i < n:
            tmp2, tmp3, tmp5 = res[p2] * 2, res[p3] * 3, res[p5] * 5
            minimum = min(tmp2, tmp3, tmp5)
            if minimum == tmp2:
                p2 += 1
            if minimum == tmp3:
                p3 += 1
            if minimum == tmp5:
                p5 += 1

            res.append(minimum)

            i += 1

        return res[-1]


if __name__ == "__main__":
    print(Solution().nthUglyNumber(10))




