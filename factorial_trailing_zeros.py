#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
"""


class Solution(object):
    def trailingZeroes(self, n):
        """
        return n // 5 + n // 25 + n // 125 + n // 3125 ...
        :type n: int
        :rtype: int
        """
        res = 0
        i = 5
        # div 5, 25, 125, 625, 3125, ... if n is larger than them
        while n // i > 0:
            res += n // i
            i *= 5

        return res



