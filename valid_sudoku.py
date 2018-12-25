#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
"""
import numpy as np


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.ans(board)

    def ans(self, board):
        m = len(board)
        if m <= 0:
            return False

        else:  # m > 0
            if not board[0]:
                return False
            else:
                n = len(board[0])

        matrix = np.array(board)

        # check row
        for row in board:
            counter = {}
            for item in row:
                if item == ".":
                    continue
                if counter.get(item) is None:
                    counter[item] = 1
                else:
                    return False

        # check col
        for j in range(n):
            counter = {}
            col = matrix[0:m, j].tolist()
            for item in col:
                if item == ".":
                    continue
                if counter.get(item) is None:
                    counter[item] = 1
                else:
                    return False

        # check 3*3
        for i in range(m//3):
            for j in range(n//3):
                box = matrix[i*3: (i+1)*3, j*3: (j+1)*3]
                box_list = box.reshape(1, -1).tolist()[0]
                counter = {}
                for item in box_list:
                    if item == ".":
                        continue
                    if counter.get(item) is None:
                        counter[item] = 1
                    else:
                        return False

        return True


if __name__ == "__main__":
    test_board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                  ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                  [".", "9", "8", ".", ".", ".", ".", "6", "."],
                  ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                  ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                  ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                  [".", "6", ".", ".", ".", ".", "2", "8", "."],
                  [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                  [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(Solution().isValidSudoku(test_board))
