#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""


class Solution(object):
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    visited = {}
    res = []

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return self.res
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not self.is_visited(i, j):
                    pacific = self.dfs(matrix, i, j, "pacific")
                    atlantic = self.dfs(matrix, i, j, "atlantic")
                    if pacific is True and atlantic is True:
                        self.res.append((i, j))
        return self.res

    def dfs(self, matrix, x, y, destination=None):
        assert destination in ("pacific", "atlantic")
        if self.on_pacific_side(x, y, matrix) and destination == "pacific":
            return True

        if self.on_atlantic_side(x, y, matrix) and destination == "atlantic":
            return True

        if self.on_pacific_side(x, y, matrix) and self.on_atlantic_side(x, y, matrix):
            return True

        self.visited[(x, y)] = True

        for direction in self.directions:
            new_x = x + direction[0]
            new_y = y + direction[1]
            if self.in_matrix(new_x, new_y, matrix) and not self.is_visited(new_x, new_y):

                if matrix[new_x][new_y] <= matrix[x][y]:
                    if self.dfs(matrix, new_x, new_y, destination) is True:
                        self.visited[(x, y)] = False
                        return True
        self.visited[(x, y)] = False

    @staticmethod
    def in_matrix(x, y, matrix):
        length = len(matrix)
        width = len(matrix[0])

        if 0 <= x < length and 0 <= y < width:
            return True
        return False

    def is_visited(self, x, y):
        if not self.visited.get((x, y)):
            return False
        return True

    @staticmethod
    def on_pacific_side(x, y, matrix):
        if x == 0 or y == 0:
            return True
        return False

    @staticmethod
    def on_atlantic_side(x, y, matrix):
        length = len(matrix)
        width = len(matrix[0])

        if x == length-1 or y == width-1:
            return True
        return False


if __name__ == "__main__":
    test_matrix = [[1, 2, 2, 3, 5],
                   [3, 2, 3, 4, 4],
                   [2, 4, 5, 3, 1],
                   [6, 7, 1, 4, 5],
                   [5, 1, 1, 2, 4]]
    test_matrix = []
    print(Solution().pacificAtlantic(test_matrix))
