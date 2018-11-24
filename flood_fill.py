#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""


class Solution(object):
    visited = {}
    directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        old_color = image[sr][sc]
        self.dfs(image, sr, sc, newColor, old_color)
        return image

    def dfs(self, image, x, y, newColor, old_color):


        for i in range(x, len(image)):
            for j in range(y, len(image[0])):

                if image[i][j] == old_color:
                    image[i][j] = newColor
                    self.visited[(i, j)] = True
                else:
                    # if image[i][j] != old_color, not connection area
                    return

                for direction in self.directions:
                    new_x = i + direction[0]
                    new_y = j + direction[1]

                    if self.in_board(new_x, new_y, image) and not self.is_visited(new_x, new_y):
                        # todo: how to judge connection?
                        # and image[i][j] == newColor
                        if image[new_x][new_y] == old_color:
                            self.dfs(image, new_x, new_y, newColor, old_color)
                # todo: necessary?
                # self.visited[(i, j)] = False

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


if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2

    image = [[0, 0, 0], [0, 0, 0]]
    sr = 1
    sc = 0
    newColor = 2

    print(Solution().floodFill(image, sr, sc, newColor))











