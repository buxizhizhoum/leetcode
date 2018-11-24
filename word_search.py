#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


class Solution(object):
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    visited = {}

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # return self.search(word, 0, board, 0, 0) is True
        return self.search_2(word, 0, board, 0, 0) is True

    def search(self, word, index, board, x, y):
        # possible to judge index == word.size()? seems not.
        # if index == len(word) - 1 and word[index] == board[x][y]:
        #     return True
        if index == len(word):
            return True

        if index > len(word):
            return False

        # todo: pay more attention here
        for i in range(x, len(board)):
            for j in range(y, len(board[0])):

                if board[i][j] == word[index]:
                    self.visited[(i, j)] = True
                    # 4 directions
                    for direction in self.directions:
                        new_x = i + direction[0]
                        new_y = j + direction[1]
                        # ensure new_x, new_y in board
                        if self.in_board(new_x, new_y, board) and not self.is_visited(new_x, new_y):
                            if self.search(word, index+1, board, new_x, new_y) is True:
                                return True
                            # else:
                            #     continue
                    self.visited[(i, j)] = False

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

    def search_2(self, word, index, board, x, y):
        """
        rewrite search, seems this is right
        :param word:
        :param index:
        :param board:
        :param x:
        :param y:
        :return:
        """
        for i in range(len(board)):
            for j in range(len(board[0])):

                if self.in_board(x, y, board) and not self.is_visited(x, y):
                    # if this point meet, search its for directions
                    if word[index] == board[x][y]:
                        if self.dfs(board, x, y, word, index) is True:
                            return True

    def dfs(self, board, x, y, word, index):
        """
        deep first search the 4 directions of a certain point
        :param board:
        :param x:
        :param y:
        :param word:
        :param index:
        :return:
        """
        # if search to the last char and the last char equals, return True
        if index == len(word) - 1 and word[index] == board[x][y]:
            return True

        self.visited[(x, y)] = True
        for direction in self.directions:
            new_x = x + direction[0]
            new_y = y + direction[1]

            if self.in_board(new_x, new_y, board) \
                    and not self.is_visited(new_x, new_y):

                if board[new_x][new_y] == word[index+1]:
                    if self.dfs(board, new_x, new_y, word, index+1) is True:
                        return True
        self.visited[(x, y)] = False
        return False


if __name__ == "__main__":
    test_board = [['A', 'B', 'C', 'E'],
                  ['S', 'F', 'C', 'S'],
                  ['A', 'D', 'E', 'E']]
    test_word = "ABCCED"

    # test_board = [
    #     ["b", "a", "b", "c", "b", "a", "b", "a", "b", "c", "a", "c", "a", "b"],
    #     ["c", "a", "c", "c", "c", "b", "a", "a", "a", "b", "c", "c", "b", "b"],
    #     ["a", "c", "c", "b", "a", "a", "b", "b", "b", "c", "c", "a", "c", "c"],
    #     ["a", "c", "b", "a", "a", "b", "c", "a", "b", "c", "b", "b", "a", "b"],
    #     ["c", "a", "a", "c", "a", "a", "a", "b", "b", "c", "a", "a", "c", "a"],
    #     ["b", "b", "a", "c", "b", "c", "c", "c", "b", "c", "a", "c", "b", "c"],
    #     ["a", "c", "a", "c", "c", "a", "c", "a", "b", "a", "c", "a", "c", "a"],
    #     ["b", "c", "a", "c", "b", "b", "c", "a", "b", "b", "a", "a", "a", "a"],
    #     ["c", "c", "c", "a", "a", "c", "b", "c", "b", "a", "a", "c", "b", "a"],
    #     ["a", "c", "a", "c", "c", "a", "c", "a", "c", "c", "b", "a", "b", "b"],
    #     ["b", "a", "c", "a", "c", "b", "b", "c", "c", "a", "a", "b", "c", "b"],
    #     ["a", "a", "c", "c", "a", "c", "b", "a", "c", "a", "b", "c", "c", "a"],
    #     ["a", "b", "c", "b", "c", "b", "b", "b", "a", "b", "c", "a", "b", "a"],
    #     ["b", "b", "c", "a", "c", "b", "c", "a", "a", "a", "b", "a", "b", "a"],
    #     ["a", "c", "a", "a", "b", "c", "c", "a", "b", "b", "c", "a", "a", "b"]]
    # test_word = "accbbcba"

    test_board = [["a"]]
    test_word = "a"
    print(Solution().exist(test_board, test_word))

    # todo: local test passed, leetcode failed.
