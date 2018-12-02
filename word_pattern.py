#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.solve(pattern, str)

    def solve(self, pattern, string):
        string_l = string.split(" ")
        if len(pattern) != len(string_l):
            return False

        s_p_map = {}  # string pattern map
        p_s_map = {}  # pattern string map
        # s is sub string in string
        for char, s in zip(pattern, string_l):
            char_buffer = s_p_map.get(s)  # get char buffered in dict
            s_buffer = p_s_map.get(char)  # get sub str buffered in dict
            if char_buffer is None:
                s_p_map[s] = char

            if s_buffer is None:
                p_s_map[char] = s

            # whether buffered char and sub str equal current one
            if char != s_p_map[s] or s != p_s_map[char]:
                return False
        return True


if __name__ == "__main__":
    test_pattern = "abba"
    test_string = "cat dog dog cat"
    # test_string = "dog dog dog dog"
    print(Solution().wordPattern(test_pattern, test_string))
