#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""


class Solution(object):
    import re
    re_compile = re.compile(r"[A-Za-z0-9]{1}")

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not len(s):
            return True

        start = 0
        end = len(s) - 1

        while start < end:
            if not self.re_compile.match(s[start]):
                start += 1
                continue

            if not self.re_compile.match(s[end]):
                end -= 1
                continue

            if s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1

        return True


if __name__ == "__main__":
    test_string = "A man, a plan, a canal: Panama"
    test_string = "0p"
    print(Solution().isPalindrome(test_string))








