#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.
"""


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        string = str(num)
        # return self.ans(string)
        # return self.recursion(string)
        return self.ans_1(num)

    def ans(self, num_str):
        str_list = list(num_str)

        while len(str_list) != 1:
            str_list = list(str(sum([int(char) for char in str_list])))

        return int("".join(str_list))

    def recursion(self, num_str):
        if len(num_str) == 1:
            return int(num_str)

        str_list = list(num_str)
        return self.recursion(str(sum([int(char) for char in str_list])))

    def ans_1(self, num):
        if num < 10:
            return num

        while num >= 10:
            tmp = 0
            while num > 0:
                tmp += num % 10
                num = num // 10
            num = tmp

        return num


if __name__ == "__main__":
    print(Solution().addDigits(100))




