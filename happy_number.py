#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        max_try_times = 900
        return self._is_happy(n, max_try_times)

    def _is_happy(self, n, try_times):
        if n == 1:
            return True
        if try_times == 0:
            return False

        string = str(n)
        sum_ = sum(int(char)**2 for char in string)

        return self._is_happy(sum_, try_times-1)


if __name__ == "__main__":
    print(Solution().isHappy(2))




