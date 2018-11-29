#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""


class Solution(object):
    vowels = ["a", "i", "o", "e", "u"]
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s

        string = list(s)
        start = 0
        end = len(s) - 1

        while start < end:
            if string[start].lower() not in self.vowels:
                start += 1

            if string[end].lower() not in self.vowels:
                end -= 1

            if string[start].lower() in self.vowels and string[end].lower() in self.vowels:
                string[start], string[end] = string[end], string[start]
                start += 1
                end -= 1

        return "".join(string)


if __name__ == "__main__":
    test_string = "hello"
    print(Solution().reverseVowels(test_string))













