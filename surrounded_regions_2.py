#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border,
which means that any 'O' on the border of the board are not flipped to 'X'.
Any 'O' that is not on the border and it is not connected to an 'O'
on the border will be flipped to 'X'. Two cells are connected if
they are adjacent cells connected horizontally or vertically.
"""


class Solution(object):
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    visited = {}
    res = []

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return

        if len(board[0]) <= 1:
            return

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and not self.on_side(i, j, board) \
                        and not self.is_visited(i, j):
                    self.dfs(board, i, j)
                    # if self.dfs(board, i, j) is not False:
                        # self.res.append((i, j))  # append is done in dfs()

        for point in self.res:
            board[point[0]][point[1]] = "X"

    def dfs(self, board, x, y):
        if self.on_side(x, y, board):
            # if on side, it means O is not surrounded by X
            return False

        self.visited[(x, y)] = True
        for direction in self.directions:
            new_x = x + direction[0]
            new_y = y + direction[1]

            if self.in_board(new_x, new_y, board) \
                    and not self.is_visited(new_x, new_y) \
                    and board[new_x][new_y] == "O":
                # todo: compare where the visited changes in other problem
                if self.dfs(board, new_x, new_y) is False:
                    return False
        self.res.append((x, y))

    def in_board(self, x, y, board):
        length = len(board)
        width = len(board[0])

        if 0 <= x < length and 0 <= y < width:
            return True
        return False

    def is_visited(self, x, y):
        if self.visited.get((x, y)) is not None:
            return True
        return False

    def on_side(self, x, y, board):
        length = len(board)
        width = len(board[0])

        if x in (0, length-1) or y in (0, width-1):
            return True
        return False


if __name__ == "__main__":
    test_board = [['X', 'X', 'X', 'X'],
                  ['X', 'O', 'O', 'X'],
                  ['X', 'X', 'O', 'X'],
                  ['X', 'O', 'X', 'X']]

    # test_board = [["O","O"],["O","O"]]
    # test_board = [["X","X","X"],["X","O","X"],["X","X","X"]]

    Solution().solve(test_board)
    print(test_board)

    # todo: local test passed, not accepted by leetcode.

