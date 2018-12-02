#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        return self.solve(points)

    def solve(self, points):
        res = 0
        for point in points:
            dis_dict = {}
            for new_point in points:
                if new_point != point:
                    distance = self.distance(point, new_point)
                    # trick
                    dis_dict[distance] = dis_dict.get(distance, 0) + 1

            for dis, number in dis_dict.iteritems():
                if number > 1:
                    res += number * (number - 1)

        return res

    def distance(self, point_1, point_2):
        return (point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2



