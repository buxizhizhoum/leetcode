#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        if root.left is not None and root.right is not None:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            return min(left, right) + 1

        # only right tree is not None
        if root.right is not None:
            right = self.minDepth(root.right)
            return right + 1
        # only left tree is not None
        elif root.left is not None:
            left = self.minDepth(root.left)
            return left + 1
        # the node is leaf node
        else:
            return 1





