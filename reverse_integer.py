#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Assume we are dealing with an environment which could only hold integers
within the 32-bit signed integer range. For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_x = str(abs(x))
        tmp_res = str_x[::-1]

        res = int(tmp_res) if x >= 0 else -int(tmp_res)
        res = res if abs(res) <= 2147483647 else 0

        return int(res)


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(132))
    print(solution.reverse(130))
    print(solution.reverse(-123))
    print(solution.reverse(-2147483648))
