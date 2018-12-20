#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        self.ans(matrix)

    def ans(self, matrix):
        if not matrix:
            return
        m = len(matrix)
        n = len(matrix[0])

        rows = set()  # store rows that contains 0
        cols = set()  # store cols that contains 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in rows:
            for j in range(n):
                matrix[i][j] = 0

        for j in cols:
            for i in range(m):
                matrix[i][j] = 0


if __name__ == "__main__":
    test_matrix = [[1, 1, 1],
                   [1, 0, 1],
                   [1, 1, 1]]
    test_matrix = [[0, 1, 2, 0],
                   [3, 4, 5, 2],
                   [1, 3, 1, 5]
                   ]

    Solution().setZeroes(matrix=test_matrix)
    print(test_matrix)

