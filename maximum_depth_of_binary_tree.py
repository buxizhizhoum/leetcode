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
        height = self.height(root)
        return height + 1

    @classmethod
    def height(cls, node):
        if node is None:
            return -1

        left = cls.height(node.left)
        right = cls.height(node.right)

        # the height of tree is growing from leaf node to root, if one of the
        # subtree is missing, the height should not be calculated
        # from the missing sub tree

        # lines below is to process the situation when a sub tree is missing,
        # it is necessary when calculate min depth, however it is
        # not necessary in max depth, since it is to find the max height, if
        # a node miss a sub tree, it will definitely not be the max height
        # if node.left is None:
        #     height = right + 1
        #     return height
        # if node.right is None:
        #     height = left + 1
        #     return height
        height = max(left + 1, right + 1)
        return height

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
