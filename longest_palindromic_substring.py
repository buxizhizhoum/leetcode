#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 1:
            return ""

        i = 0
        size = 0
        start, end = 0, 0
        while i < len(s):
            size_tmp = self.search(s, i, i)
            if size_tmp > size:
                size = size_tmp
                start = i - size / 2
                end = i + size / 2

            size_tmp = self.search(s, i, i+1)
            if size_tmp > size:
                size = size_tmp
                start = i - (size / 2 - 1) - 1
                end = i + size / 2 + 1
            i += 1
        return s[start: end + 1]

    @staticmethod
    def search(s, left, right):
        size = 0
        # start, end = left, right
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                if (right - left) > size:
                    size = right - left
                left -= 1
                right += 1
            else:
                break

        return size


if __name__ == "__main__":
    string = "abababa"
    string = "abbabbaba"
    # string = "babad"
    string = "a"
    s = Solution()
    print(s.longestPalindrome(string))

