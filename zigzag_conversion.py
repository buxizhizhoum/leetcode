#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = []
        for i in range(numRows):
            if i == 0:
                # rownum + (rownum - 2)
                # get item in the first row, k[rownum + (rownum - 2)]
                k = 0
                while k < len(s) / float(numRows):
                    index = k * (numRows + (numRows - 2))
                    if index < len(s):
                        res.append(s[index])
                        # print(s[index])
                    k += 1

            elif i == numRows - 1:
                # rownum + (rownum - 2) + rownum - 1
                k = 0
                while k < len(s) / float(numRows):
                    index = k * (numRows + (numRows - 2)) + numRows - 1
                    if index < len(s):
                        res.append(s[index])
                        # print s[index]
                    k += 1
                # pass
            else:
                # rownum + (rownum - 2) + i
                # [rownum + (rownum - 2)] + (rownum - 1) + (rownum - 1) - i
                k = 0
                while k < len(s) / float(numRows):
                    index = k * (numRows + (numRows - 2)) + i
                    if index < len(s):
                        res.append(s[index])
                        # print s[index]

                    index = k * (numRows + (numRows - 2)) + (numRows - 1) + (numRows -1) - i
                    if index < len(s):
                        res.append(s[index])
                        # print s[index]

                    k += 1
        return "".join([str(item) for item in res])


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    s = "PAYPALISHIRING"
    s = "A"
    s = "AB"
    rows = 1
    solution = Solution()
    print(solution.convert(s, rows))
