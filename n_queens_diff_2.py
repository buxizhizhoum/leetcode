#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        col = [False for _ in range(n)]
        diagonal1 = [False for _ in range(2 * n - 1)]
        diagonal2 = [False for _ in range(2 * n - 1)]

        res = [0]
        answer = []
        # for i in range(n):
        self.dfs(n, 0, res, answer, col, diagonal1, diagonal2)
        return res[0]

    def dfs(self, n, i, res, answer, col, diagonal1, diagonal2):
        if i == n:
            res[0] += 1
            return

        # j are in range(n), and will not be out of board
        for j in range(n):
            if not col[j] and not diagonal1[i+j] and not diagonal2[i-j+n-1]:
                col[j] = True
                diagonal1[i + j] = True
                diagonal2[i - j + n - 1] = True

                self.dfs(n, i+1, res, answer+[(i, j)], col, diagonal1, diagonal2)

                diagonal2[i - j + n - 1] = False
                diagonal1[i + j] = False
                col[j] = False
        return


if __name__ == "__main__":
    print(Solution().totalNQueens(4))






