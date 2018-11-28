#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return

        cache = 1  # simulate to add 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + cache < 10:
                cache = 0
                digits[i] += 1
                break

            else:
                tmp = digits[i]
                digits[i] = (tmp + 1) % 10
                cache = (tmp + 1) // 10

        if cache != 0:
            digits.insert(0, cache)
        return digits


if __name__ == "__main__":
    test_input = [1, 2, 3]
    test_input = [7,8,9,9]
    test_input = [9]
    Solution().plusOne(test_input)
    print(test_input)










