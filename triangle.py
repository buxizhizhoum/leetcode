#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        height = len(triangle)
        if height == 0:
            return 0
        # return self.recursion_version(triangle, 0, 0, height)
        # cache = [[float("-inf") for _ in range(len(triangle[j]))] for j in range(len(triangle))]
        # return self.recursion_with_cache(triangle, 0, 0, height, cache)
        return self.dynamic_programming(triangle, height)

    def recursion_version(self, triangle, i, j, height):
        if i == height - 1:
            return triangle[i][j]

        return triangle[i][j] + min(self.recursion_version(triangle, i+1, j, height), self.recursion_version(triangle, i+1, j+1, height))

    def recursion_with_cache(self, triangle, i, j, height, cache):
        """
        recursion with cache
        :param triangle:
        :param i:
        :param j:
        :param height:
        :param cache: a nested list used to cache calculated result.
        :return:
        """
        if cache[i][j] != float("-inf"):
            return cache[i][j]

        if i == height - 1:
            cache[i][j] = triangle[i][j]
            return triangle[i][j]

        cache[i][j] = triangle[i][j] + min(self.recursion_with_cache(triangle, i+1, j, height, cache),
                                           self.recursion_with_cache(triangle, i+1, j+1, height, cache))
        return cache[i][j]

    def dynamic_programming(self, triangle, height):

        cache = [[float("-inf") for _ in range(len(triangle[j]))] for j in range(len(triangle))]
        # initialize base condition, stop condition in recursion
        for j in range(len(triangle[height-1])):
            cache[height-1][j] = triangle[height-1][j]

        for i in range(height-2, -1, -1):
            for j in range(i+1):
                cache[i][j] = triangle[i][j] + min(cache[i+1][j], cache[i+1][j+1])
        return cache[0][0]


if __name__ == "__main__":
    test_triangle = [
                         [2],
                        [3,4],
                       [6,5,7],
                      [4,1,8,3]
                    ]
    print(Solution().minimumTotal(test_triangle))


