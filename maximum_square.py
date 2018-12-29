#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        return self.brute_force(matrix)

    def brute_force(self, matrix):
        m = len(matrix)
        if m < 1:
            return 0
        n = len(matrix[0])

        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    continue

                # search the max square contain this 1
                res = max(res, self.search_square(matrix, i, j))
        return res * res  # return all element, res is side length

    def search_square(self, matrix, i, j):
        """
        search the max square that could generate based on matrix[i][j]

        matrix[i][j] should be 1
        :param matrix:
        :param i:
        :param j:
        :return:
        """
        m = len(matrix)
        if m < 1:
            return 0
        n = len(matrix[0])

        if matrix[i][j] == "0":
            return 0

        size = 1  # since matrix[i][j] == 1, initial size is 1
        k = i + 1  # start form right bottom element of current element
        l = j + 1
        while k < m and l < n:
            # stop when 0 is founded
            if matrix[k][l] == "0":
                break

            else:
                # check other element in range[i, k) [j, l)
                # if there is only one "0", break

                # check element in column l, row in range[i, k)
                if not self.col_chk(matrix, i, k, l):
                    break
                # check element in row k, col in range [j, l)
                if not self.row_chk(matrix, j, k, l):
                    break

                size += 1

            k += 1
            l += 1
        return size

    def col_chk(self, matrix, i, k, l):
        """
        check element in column l, row in range[i, k)
        :param matrix:
        :param i:
        :param k:
        :param l:
        :return: True if all is "1", else False
        """
        for p in range(i, k):
            if matrix[p][l] == "0":
                return False
        return True

    def row_chk(self, matrix, j, k, l):
        """
        check element in row k, col in range [j, l)
        :param matrix:
        :param j:
        :param k:
        :param l:
        :return: True if all is "1", else False
        """
        for q in range(j, l):
            if matrix[k][q] == "0":
                return False
        return True


if __name__ == "__main__":
    test_matrix = [["1", "0", "1", "0", "0"],
                   ["1", "0", "1", "1", "1"],
                   ["1", "1", "1", "1", "1"],
                   ["1", "0", "0", "1", "0"]]
    # test_matrix = [["0"]]
    print(Solution().maximalSquare(test_matrix))
