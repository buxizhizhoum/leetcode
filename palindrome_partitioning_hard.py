#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""


class Solution(object):
    min_cut = float("inf")
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        path = []
        length = len(s)
        self.find_palindrome(path, s, length)
        return self.min_cut - 1

    def find_palindrome(self, path, s, length):
        path_len = sum([len(item) for item in path])
        if path_len == length:
            current_cut = len(path)
            if self.min_cut > current_cut:
                self.min_cut = current_cut
            return

        for i in range(1, len(s) + 1):
            current_str = s[:i]
            if not self.is_palindrome(current_str):
                continue

            self.find_palindrome(path + [current_str], s[i:], length)

    def is_palindrome(self, string):
        """
        judge whether a string is palindrome
        :param string:
        :return:
        """
        start, end = 0, len(string) - 1
        while start <= end:
            if string[start] == string[end]:
                start += 1
                end -= 1
                continue
            else:
                return False
        return True


if __name__ == "__main__":
    test_string = "ababababababababababababcbabababababababababababa"
    print(Solution().minCut(test_string))

    # todo: time limit exceeded.







