#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    height = 0

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.recursion(root)
        return self.height

    def recursion(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 0

        l = self.recursion(root.left)
        r = self.recursion(root.right)
        if root.left is not None:
            if root.val == root.left.val:
                l += 1
            else:
                # this is to break the height increase if val does not equal
                # however the largest height info is already buffed in self.height
                l = 0

        if root.right is not None:
            if root.val == root.right.val:
                r += 1
            else:
                r = 0

        self.height = max(self.height, l + r)
        return max(l, r)


if __name__ == "__main__":
    values = [5,4,5,1,2,3,5]
    values = [5,4,5,1,1,5]
    values = [1,4,5,4,4,5]
    from tools.construct_binary_tree import Construction
    root = Construction(values).construct()
    print(Solution().longestUnivaluePath(root))

