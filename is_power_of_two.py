#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.ans_1(n)

    def ans_1(self, n):
        if n == 0:
            return False
        if n == 1:
            return True

        if n % 2 != 0:
            return False

        return self.ans_1(n // 2)


if __name__ == "__main__":
    test_n = 1024
    print(Solution().isPowerOfTwo(test_n))

