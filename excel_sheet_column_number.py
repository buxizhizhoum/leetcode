#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""


class Solution(object):
    cache = {'A': 1, 'C': 3, 'B': 2, 'E': 5, 'D': 4, 'G': 7, 'F': 6, 'I': 9,
             'H': 8, 'K': 11, 'J': 10, 'M': 13, 'L': 12, 'O': 15, 'N': 14,
             'Q': 17, 'P': 16, 'S': 19, 'R': 18, 'U': 21, 'T': 20, 'W': 23,
             'V': 22, 'Y': 25, 'X': 24, 'Z': 26}

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        res = 0
        # i start from end, index start from start to get char from beginning
        for i in range(length-1, -1, -1):
            # start from beginning, is used to get value from dict
            index = length - 1 - i
            digit = self.cache.get(s[index])
            # i start from beginning, is the pow of corresponding char
            res += pow(26, i) * digit

        return res


if __name__ == "__main__":
    for string in ("A", "AA", "AB", "ZY", "ADT"):
        print(Solution().titleToNumber(string))

