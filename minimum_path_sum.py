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

        cache = [[float("inf") for _ in range(len(grid[i]))] for i in range(len(grid))]
        res = float("inf")
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                min_sum = self.dfs(grid, 0, 0, cache)
                res = min(res, min_sum)
        return res

    def dfs(self, grid, x, y, cache):
        if cache[x][y] != float("inf"):
            return cache[x][y]
        if x == len(grid) - 1 and y == len(grid[0]) - 1:
            return grid[x][y]

        min_res = float("inf")
        for direction in self.directions:
            new_x = x + direction[0]
            new_y = y + direction[1]

            if self.in_grid(new_x, new_y, grid):
                tmp_sum = self.dfs(grid, new_x, new_y, cache) + grid[x][y]
                min_res = min(min_res, tmp_sum)
        cache[x][y] = min_res
        return cache[x][y]

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
    test_input = [[1, 2],
                  [1, 1]]
    print(Solution().minPathSum(test_input))
