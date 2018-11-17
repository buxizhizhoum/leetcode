#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left_height = self.maxDepth(root.left)
        right_heght = self.maxDepth(root.right)
        return max(left_height, right_heght) + 1
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == "__main__":
    r = TreeNode(6)
    r.left = TreeNode(5)
    r.right = TreeNode(9)

    # r.left.left = TreeNode(3)
    # r.left.left.left = TreeNode(3)
    # r.left.right = TreeNode(4)

    r.right.left = TreeNode(7)
    r.right.right = TreeNode(11)
    r.right.right.right = TreeNode(13)

    s = Solution()
    res = s.maxDepth(r)
    print(res)
