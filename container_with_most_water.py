#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given n non-negative integers a1, a2, ..., an , where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        max_area = 0
        while i != j:
            h = min(height[i], height[j])
            w = j - i
            area = w * h
            max_area = max(max_area, area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area


if __name__ == "__main__":
    input_l = [1,8,6,2,5,4,8,3,7]
    solution = Solution()
    print(solution.maxArea(input_l))



