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
        dialog1 = [False for _ in range(2 * n - 1)]
        dialog2 = [False for _ in range(2 * n - 1)]

        res = [0]
        answer = []
        # for i in range(n):
        self.dfs(n, 0, res, answer, col, dialog1, dialog2)
        return res[0]

    def dfs(self, n, i, res, answer, col, dialog1, dialog2):
        if i == n:
            res[0] += 1
            return

        # j are in range(n), and will not be out of board
        for j in range(n):
            if not col[j] and not dialog1[i+j] and not dialog2[i-j+n-1]:
                col[j] = True
                dialog1[i + j] = True
                dialog2[i - j + n - 1] = True

                self.dfs(n, i+1, res, answer+[(i, j)], col, dialog1, dialog2)

                dialog2[i - j + n - 1] = False
                dialog1[i + j] = False
                col[j] = False
        return


if __name__ == "__main__":
    print(Solution().totalNQueens(4))






