#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needle_len = len(needle)
        str_len = len(haystack)

        if haystack == needle:
            return 0

        for index in range(str_len - needle_len + 1):
            if haystack[index: index + needle_len] == needle:
                return index
        return -1


if __name__ == "__main__":
    # test_str = "Hello World!"
    # cursor = "ll"
    test_str = "mississippi"
    cursor = "pi"
    print Solution().strStr(test_str, cursor)
