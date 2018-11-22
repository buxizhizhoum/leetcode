#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        buffer_s_t = {}
        buffer_t_s = {}
        # return self._is_isomorphic(s, t, buffer_s_t, buffer_t_s)
        # return self._is_isomorphic_2(s, t, buffer_s_t)
        return self._is_isomorphic_3(s, t, buffer_s_t, buffer_t_s)

    def _is_isomorphic(self, s, t, buffer_s_t, buffer_t_s):
        """
        backtracking version, two dict to buffer, memory limit exceeded.
        :param s:
        :param t:
        :param buffer_s_t:
        :param buffer_t_s:
        :return:
        """
        if len(s) == 0 and len(t) == 0:
            return True

        char_s = s[0]
        char_t = t[0]
        if char_s not in buffer_s_t and char_t not in buffer_t_s:
            buffer_s_t[char_s] = char_t
            buffer_t_s[char_t] = char_s

            return self._is_isomorphic(s[1:], t[1:], buffer_s_t, buffer_t_s)
        elif (buffer_s_t.get(char_s) and buffer_t_s.get(char_t)) is None:
            return False
        elif buffer_s_t[char_s] == char_t and buffer_t_s[char_t] == char_s:
            return self._is_isomorphic(s[1:], t[1:], buffer_s_t, buffer_t_s)

        else:
            return False

    def _is_isomorphic_2(self, s, t, buffer_s_t):
        """
        backtracking version, one dict to buffer, memory limit exceeded.
        :param s:
        :param t:
        :param buffer_s_t:
        :return:
        """
        if len(s) == 0 and len(t) == 0:
            return True

        char_s = s[0]
        char_t = t[0]
        if char_s not in buffer_s_t:
            if char_t not in buffer_s_t.values():
                buffer_s_t[char_s] = char_t
                return self._is_isomorphic_2(s[1:], t[1:], buffer_s_t)
            else:
                return False
        elif buffer_s_t.get(char_s) is None:
            return False
        elif buffer_s_t[char_s] == char_t:
            return self._is_isomorphic_2(s[1:], t[1:], buffer_s_t)

        else:
            return False

    def _is_isomorphic_3(self, s, t, buffer_s_t, buffer_t_s):
        """
        loop version, the memory limit exceeded problem is solved.
        :param s:
        :param t:
        :param buffer_s_t:
        :param buffer_t_s:
        :return:
        """
        for index in range(len(s)):
            char_s = s[index]
            char_t = t[index]
            # both not in buffer
            if char_s not in buffer_s_t and char_t not in buffer_t_s:
                buffer_s_t[char_s] = char_t
                buffer_t_s[char_t] = char_s
                continue
            # one is in buffer
            # elif (char_s in buffer_s_t and char_t in buffer_t_s) is False:
            elif (buffer_s_t.get(char_s) and buffer_t_s.get(char_t)) is None:
                return False
            # both in buffer
            elif buffer_s_t[char_s] == char_t and buffer_t_s[char_t] == char_s:
                continue
            else:
                return False
        return True


if __name__ == "__main__":
    s = "ab"
    t = "aa"
    print(Solution().isIsomorphic(s, t))











