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

        cache = [[0 for j in range(n)] for i in range(m)]

        # initialize last row
        for j in range(n):
            cache[m-1][j] = int(matrix[m-1][j])
        # initialize last col
        for i in range(m):
            cache[i][n-1] = int(matrix[i][n-1])

        # dynamic programming
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if matrix[i][j] == "0":
                    cache[i][j] = 0
                else:
                    # min(right_bottom, right, bottom))
                    cache_res = min(cache[i+1][j+1], cache[i+1][j], cache[i][j+1])
                    if cache_res == 0:
                        # 1  0
                        # 1  1
                        # if minimum of right_bottom, right, bottom is 0,
                        # this element is 1, the minimum square is element itself
                        cache[i][j] = 1
                    else:
                        # 1  1
                        # 2  1
                        # the max square is min(right_bottom, right, bottom)+1
                        cache[i][j] = cache_res + 1

        # find result
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, cache[i][j])

        return res*res


if __name__ == "__main__":
    test_matrix = [["1", "0", "1", "0", "0"],
                   ["1", "0", "1", "1", "1"],
                   ["1", "1", "1", "1", "1"],
                   ["1", "0", "0", "1", "0"]]
    # test_matrix = [["0"]]
    test_matrix = [["1", "1", "1", "0", "0"],
                   ["1", "1", "1", "0", "0"],
                   ["1", "1", "1", "1", "1"],
                   ["0", "1", "1", "1", "1"],
                   ["0", "1", "1", "1", "1"],
                   ["0", "1", "1", "1", "1"]]
    print(Solution().maximalSquare(test_matrix))

    # todo: cache should start from right bottom
