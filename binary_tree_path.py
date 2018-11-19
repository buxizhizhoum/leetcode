#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if root is None:
            return res

        if root.left is None and root.right is None:
            res.append(str(root.val))
            return res

        # logic start
        left_path = self.binaryTreePaths(root.left)
        right_path = self.binaryTreePaths(root.right)

        for item in left_path:
            res.append(str(root.val) + "->" + item)

        for item in right_path:
            res.append(str(root.val) + "->" + item)

        return res







