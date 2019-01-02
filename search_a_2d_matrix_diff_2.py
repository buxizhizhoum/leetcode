#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""
import numpy as np


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return self.search(matrix, target)

    def search(self, matrix, target):
        """
        binary search each row, O(nlogm)
        :param matrix:
        :param target:
        :return:
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        array = np.array(matrix)

        i = 0
        while i < m:
            tmp = self.binary_search(array[i][:], target)
            if tmp is True:
                return True
            i += 1

        return False

    def binary_search(self, nums, target):
        if len(nums) == 0:
            return False

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True

            elif nums[mid] < target:
                l = mid + 1
            else:  # nums[mid] > target
                r = mid - 1

        return False

    def search_1(self, matrix, target):
        """
        start search from top right,
        if the target is greater than the value in current position,
        then the target can not be in entire row of current position because the row is sorted,
        if the target is less than the value in current position,
        then the target can not in the entire column because the column is sorted too.
        We can rule out one row or one column each time, so the time complexity is O(m+n).

        refer: https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/66140/My-concise-O(m+n)-Java-solution
        :param matrix:
        :param target:
        :return:
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        row = 0
        col = n-1
        while row < m and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                row += 1
            else:  # target < matrix[row][col]
                col -= 1

        return False


if __name__ == "__main__":
    test_matrix = [[1, 4, 7, 11, 15],
                   [2, 5, 8, 12, 19],
                   [3, 6, 9, 16, 22],
                   [10, 13, 14, 17, 24],
                   [18, 21, 23, 26, 30]]
    target = 9
    print(Solution().searchMatrix(test_matrix, target))
    print(Solution().search_1(test_matrix, target))
