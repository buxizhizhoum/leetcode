#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""


class Solution(object):
    directions = [[1, 0], [0, 1]]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return
        length = len(grid)
        width = len(grid[0])
        return self.dynamic_programming(grid, length, width)

    def dynamic_programming(self, grid, length, width):
        cache = [[float("inf") for _ in range(len(grid[i]))]
                 for i in range(len(grid))]

        cache[length - 1][width - 1] = grid[length - 1][width - 1]

        for i in range(length - 1, -1, -1):
            for j in range(width - 1, -1, -1):

                if i == length - 1 and j == width - 1:
                    cache[length - 1][width - 1] = grid[length - 1][width - 1]
                    continue

                min_res = float("inf")
                for direction in self.directions:
                    new_x = i + direction[0]
                    new_y = j + direction[1]

                    if self.in_grid(new_x, new_y, grid):
                        min_res = min(min_res, cache[new_x][new_y] + grid[i][j])

                cache[i][j] = min_res
        return cache[0][0]

    @staticmethod
    def in_grid(x, y, grid):
        length = len(grid)
        width = len(grid[0])

        if 0 <= x < length and 0 <= y < width:
            return True
        return False


if __name__ == "__main__":
    test_input = [[1, 3, 1],
                  [1, 5, 1],
                  [4, 2, 1]]
    # test_input = [[1, 2],
    #               [1, 1]]
    print(Solution().minPathSum(test_input))
