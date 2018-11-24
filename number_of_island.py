#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""


class Solution(object):
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    visited = {}
    res = 0

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # self.find_island(grid, 0, 0)
        res = self.find_island_2(grid, 0, 0)
        # return self.res
        return res

    def find_island(self, grid, x, y):
        """
        this is a wrong answer
        :param grid:
        :param x:
        :param y:
        :return:
        """
        if self.is_visited(x, y):
            return

        for i in range(x, len(grid)):
            for j in range(y, len(grid[0])):

                if grid[x][y] == "1":
                    if not self.is_visited(i, j):
                        self.res += 1
                    else:
                        continue

                self.visited[(i, j)] = True

                for direction in self.directions:
                    new_x = i + direction[0]
                    new_y = j + direction[1]

                    if self.in_board(new_x, new_y, grid) and not self.is_visited(new_x, new_y):
                        if grid[x][y] == "1":  # is island
                            self.find_island(grid, new_x, new_y)

    def in_board(self, i, j, board):
        length = len(board)
        width = len(board[0])

        if 0 <= i < length and 0 <= j < width:
            return True
        return False

    def is_visited(self, i, j):
        if self.visited.get((i, j)) is None:
            return False
        return True

    def find_island_2(self, grid, x, y):
        """
        this works on local, leetcode not accept yet.
        :param grid:
        :param x:
        :param y:
        :return:
        """
        if self.is_visited(x, y):
            return

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                # if it is island and have not been visited,
                # means find another new start
                if grid[i][j] == "1" and not self.is_visited(i, j):
                    self.res += 1
                    res += 1

                    # will find all connecting island with grid[i][j]
                    self.dfs(grid, i, j)
        return res

    def dfs(self, grid, i, j):
        """
        deep first search
        :param grid:
        :param i:
        :param j:
        :return:
        """
        # todo: Attention:
        # the difference with word search is that
        # there is no procedure to set visited to false
        self.visited[(i, j)] = True

        for direction in self.directions:
            new_x = i + direction[0]
            new_y = j + direction[1]

            if self.in_board(new_x, new_y, grid) \
                    and not self.is_visited(new_x, new_y):
                # if new point is island, continue to search from this point
                if grid[i][j] == "1":
                    self.dfs(grid, new_x, new_y)
        return


if __name__ == "__main__":
    Input = ["11110",
             "11010",
             "11000",
             "00001"]
    Input = [["1", "1", "0", "0", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "1", "0", "0"],
             ["0", "0", "0", "1", "1"]]
    Input = [["1", "1", "0", "0", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "1", "0", "0"],
             ["0", "0", "0", "1", "1"]]
    print(Solution().numIslands(Input))
