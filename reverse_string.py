#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Write a function that takes a string as input and returns the string reversed.

Example 1:

Input: "hello"
Output: "olleh"
Example 2:

Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
        # return self.two_pointer(s)

    def two_pointer(self, s):
        if len(s) < 2:
            return s

        start = 0
        end = len(s) - 1

        string = list(s)

        while start < end:
            string[start], string[end] = string[end], string[start]
            start += 1
            end -= 1

        return "".join(string)


if __name__ == "__main__":
    test_s = "hello"
    print(Solution().reverseString(test_s))




