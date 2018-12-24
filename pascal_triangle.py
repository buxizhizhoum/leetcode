#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        return self.ans(numRows)

    def ans(self, numRows):
        res = []
        # initialize res
        for i in range(numRows):
            line = []
            for j in range(i+1):
                if j == 0 or j == i:
                    line.append(1)
                else:
                    line.append(None)

            res.append(line)

        # calculate
        for index, line in enumerate(res[2:], start=2):
            for i in range(1, index):
                # add element of line above
                line[i] = res[index-1][i-1] + res[index-1][i]

        return res


if __name__ == "__main__":
    print(Solution().generate(5))


