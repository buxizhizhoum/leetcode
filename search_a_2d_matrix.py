#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return self.ans(matrix, target)

    def ans(self, matrix, target):
        if not matrix:
            return False

        m = len(matrix)
        if m > 0:
            n = len(matrix[0])
            if n == 0:
                return False

        target_row = None
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][n-1]:
                target_row = i
                break

        if target_row is not None:
            return self._binary_search(matrix[target_row], 0, n, target)
        return False

    def _binary_search(self, data, start, end, target):
        if start > end:
            return False

        mid = start + (end - start) // 2
        if data[mid] == target:
            return True

        if target < data[mid]:
            return self._binary_search(data, start, mid-1, target)
        else:
            return self._binary_search(data, mid+1, end, target)


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7],
              [10, 11, 16, 20],
              [23, 30, 34, 50]]
    target = 13
    print(Solution().searchMatrix(matrix, target))
