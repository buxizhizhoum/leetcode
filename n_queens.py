#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col = [False for _ in range(n)]
        dialog1 = [False for _ in range(2 * n - 1)]
        dialog2 = [False for _ in range(2 * n - 1)]

        res = []
        answer = []
        # for i in range(n):
        self.dfs(n, 0, res, answer, col, dialog1, dialog2)
        board = self.generate_result(n, res)
        return board

    def dfs(self, n, i, res, answer, col, dialog1, dialog2):
        if i == n:
            res.append(answer)
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

    def generate_result(self, n, res):
        boards = []
        for answer in res:
            board_tmp = [["." for _ in range(n)] for _ in range(n)]
            for point in answer:
                board_tmp[point[0]][point[1]] = "Q"
            boards.append(board_tmp)

        result = []
        for board in boards:
            tmp = []
            for line in board:
                line = "".join(line)
                tmp.append(line)
            result.append(tmp)

        return result


if __name__ == "__main__":
    print(Solution().solveNQueens(4))



