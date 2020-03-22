#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a matrix of m x n elements (m rows, n columns), return all elements
of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution(object):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return

        m = len(matrix)
        n = len(matrix[0])

        visited = [[False for j in range(n)] for i in range(m)]

        return self.recursive(matrix, 0, 0, 0, m, n, visited)

    def valid(self, x, y, m, n, visited):
        if 0 <= y < n and 0 <= x < m and not visited[x][y]:
            return True
        return False

    def new_start(self, direction_i, x, y):
        # calculate new start point
        new_direction = self.directions[(direction_i + 1) % 4]
        x += new_direction[1]
        y += new_direction[0]
        return x, y

    def recursive(self, matrix, direction_i, x, y, m, n, visited):
        if not self.valid(x, y, m, n, visited):
            return []

        tmp = []
        # get real directions
        direction = self.directions[direction_i % 4]
        while self.valid(x, y, m, n, visited):
            visited[x][y] = True

            point = matrix[x][y]
            tmp.append(point)

            x += direction[1]
            y += direction[0]

        # 抵消while循环最后一次加的x, y
        x -= direction[1]
        y -= direction[0]
        x, y = self.new_start(direction_i, x, y)

        res = tmp + self.recursive(matrix, direction_i + 1, x, y, m, n, visited)
        return res


if __name__ == "__main__":
    test_matrix = [[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]]
    solution = Solution()
    print solution.spiralOrder(test_matrix)




