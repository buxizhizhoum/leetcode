#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        path = []
        length = len(s)
        self.find_palindrome_2(res, path, s, length)
        return res

    def find_palindrome(self, res, path, s, length):
        """
        find palindrome partition
        :param res: a list
        :param path: a list
        :param s: a string
        :param length: length of original string
        :return:
        """
        # all legth of path
        path_length = sum([len(item) for item in path])
        if path_length == length:
            res.append(path)
            return

        for i in range(1, len(s) + 1):
            current_str = s[:i]
            # judge whether palindrome on s[:i]
            # when length is 1, it is palindrome definitely
            if not self.is_palindrome(current_str):
                continue

            # update path is done when passing parameter
            self.find_palindrome(res, path + [current_str], s[i:], length)

    def find_palindrome_2(self, res, path, s, length):
        """
        find palindrome partition
        :param res: a list
        :param path: a list
        :param s: a string
        :param length: length of original string
        :return:
        """
        # all legth of path
        path_length = sum([len(item) for item in path])
        import copy
        if path_length == length:
            # todo: Attention: copy should be used, otherwise res will be changed when path is changed
            tmp = copy.copy(path)
            res.append(tmp)
            return

        for i in range(1, len(s) + 1):
            current_str = s[:i]
            # judge whether palindrome on s[:i]
            # when length is 1, it is palindrome definitely
            if not self.is_palindrome(current_str):
                continue

            # todo: Attention: if path.append, path.pop is needed after recur
            path.append(current_str)
            # self.find_palindrome(res, path + [current_str], s[i:], length)
            self.find_palindrome_2(res, path, s[i:], length)
            path.pop()

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
    test_string = "aab"
    print(Solution().partition(test_string))




