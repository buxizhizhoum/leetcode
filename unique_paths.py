#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""


class Solution(object):
    directions = [[0, 1], [1, 0]]  # right and down

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        cache = [[-1 for _ in range(m)] for i in range(n)]
        # this question do not need to start from every point in the grid
        # so there is not 2 level for loop
        # return self.dfs(0, 0, m, n, cache)
        return self.dynamic_programming(m, n)

    def dfs(self, i, j, m, n, cache):
        # if reach the right bottom point, return
        # todo: Attention m and n here
        if i == n-1 and j == m-1:
            cache[n-1][m-1] = 0
            return 1
        # point on right side have only one path to right bottom
        if i == n-1 and j != m-1:
            return 1
        # point on bottom side have only one path to right bottom
        if i != n-1 and j == m-1:
            return 1

        if cache[i][j] != -1:
            return cache[i][j]

        res = 0
        for direction in self.directions:
            new_x = i + direction[0]
            new_y = j + direction[1]

            if self.in_grid(new_x, new_y, m, n):
                res += self.dfs(new_x, new_y, m, n, cache)

        cache[i][j] = res
        return res

    @staticmethod
    def in_grid(x, y, m, n):
        if 0 <= x < n and 0 <= y < m:
            return True
        return False

    def dynamic_programming(self, m, n):
        if m == 1 or n == 1:
            return 1
        cache = [[1 if j == m-1 or i == n-1 else -1 for j in range(m)]
                 for i in range(n)]

        # n row m col
        # drive to base condition with loop first
        for i in range(n - 2, -1, -1):
            for j in range(m-2, -1, -1):

                res = 0
                for direction in self.directions:
                    new_x = i + direction[0]
                    new_y = j + direction[1]

                    res += cache[new_x][new_y]
                cache[i][j] = res
        return cache[0][0]


if __name__ == "__main__":
    m = 3
    n = 2
    m = 7
    n = 3
    print(Solution().uniquePaths(m, n))

