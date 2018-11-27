#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""


class Solution(object):
    directions = [[0, 1], [1, 0]]  # right and down

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        return self.dynamic_programming(m, n, obstacleGrid)




    def dynamic_programming(self, m, n, grid):
        """
        m is col number n is row number
        :param m:
        :param n:
        :return:
        """
        if n == 1:
            if 1 in grid[0]:
                return 0
            else:
                return 1

        if m == 1:
            right_line = []
            for i in range(n):
                right_line.append(grid[i][0])
            if 1 in right_line:
                return 0
            else:
                return 1

        if grid[0][0] == 1:
            return 0

        cache = self.initialize_cache(m, n, grid)
        # n row m col
        # drive to base condition with loop first
        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):

                res = 0
                for direction in self.directions:
                    new_x = i + direction[0]
                    new_y = j + direction[1]

                    if grid[new_x][new_y] == 0:
                        res += cache[new_x][new_y]

                cache[i][j] = res

        return cache[0][0]

    @staticmethod
    def initialize_cache(m, n, grid):
        # initialize cache
        cache = [[1 if j == m - 1 or i == n - 1 else -1 for j in range(m)]
                 for i in range(n)]
        # update base condition according to obstacle
        bottom_line = grid[n - 1]
        right_line = []
        for i in range(len(grid)):
            right_line.append(grid[i][-1])

        if 1 in bottom_line:
            # obstacle_index_bottom = bottom_line.index(1)
            for i in range(m):
                cache[n - 1][i] = 0
        if 1 in right_line:
            # obstacle_index_right = right_line.index(1)
            # cache[:][obstacle_index_right:] = 0
            for i in range(len(cache)):
                cache[i][-1] = 0

        return cache

if __name__ == "__main__":
    test_input = [[0, 0, 0],
                  [0, 1, 0],
                  [0, 0, 0]]
    test_input = [[0],[1]]
    test_input = [[1,0],[0,0]]
    print(Solution().uniquePathsWithObstacles(test_input))

    # todo: test not passed


