#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""


class Solution(object):
    cache = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H",
             9: "I", 10: "J", 11: "K", 12: "L", 13: "M", 14: "N", 15: "O",
             16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V",
             23: "W", 24: "X", 25: "Y", 26: "Z"}

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        return self.recursion(n)

    def recursion(self, n):

        div, mod = divmod(n, 26)

        if mod == 0:
            div -= 1
            mod = 26

        if div > 26:
            return self.recursion(div) + self.cache.get(mod)

        elif div > 0:
            return self.cache.get(div) + self.cache.get(mod)
        elif div == 0:
            return self.cache.get(mod)

if __name__ == "__main__":
    for i in range(1, 26):
        print(Solution().convertToTitle(i))

    for i in (701, 702, 800):
        print(Solution().convertToTitle(i))

