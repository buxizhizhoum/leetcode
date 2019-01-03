#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle
defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1)
and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
"""


class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.memo = self.cache()

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.calculate(row1, col1, row2, col2)

    def calculate(self, row1, col1, row2, col2):
        # self.memo[row1][col1] is in self.memo[row1][col2+1] - self.memo[row2+1][col1]
        # it is sub two times
        res = self.memo[row2+1][col2+1] \
              - self.memo[row1][col2+1] \
              - self.memo[row2+1][col1] \
              + self.memo[row1][col1]
        return res

    def cache(self):
        m = len(self.matrix)
        if m == 0:
            return

        n = len(self.matrix[0])
        if n == 0:
            return

        # the first element is sentinel
        memo = [[0 for j in range(n+1)] for i in range(m+1)]
        # prepare prefix sum, memo[0][:] memo[:][0] is sentinel
        for j in range(1, n+1):
            # the first row
            memo[1][j] = self.matrix[0][j-1] + memo[1][j-1]

        for i in range(1, m+1):
            # the first col
            memo[i][1] = self.matrix[i-1][0] + memo[i-1][1]

        for i in range(2, m+1):
            for j in range(2, n+1):
                memo[i][j] = memo[i-1][j] + memo[i][j-1] - memo[i-1][j-1] + self.matrix[i-1][j-1]

        return memo


if __name__ == "__main__":
    # Your NumMatrix object will be instantiated and called as such:
    test_matrix = [[3, 0, 1, 4, 2],
                   [5, 6, 3, 2, 1],
                   [1, 2, 0, 1, 5],
                   [4, 1, 0, 1, 7],
                   [1, 0, 3, 0, 5]]
    row1, col1, row2, col2 = 2, 1, 4, 3

    # test_matrix = [[-4,-5]]
    # row_cols = ([0,0,0,0],[0,0,0,1],[0,1,0,1])
    obj = NumMatrix(test_matrix)
    param_1 = obj.sumRegion(row1, col1, row2, col2)
    print(param_1)



