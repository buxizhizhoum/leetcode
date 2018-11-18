#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.is_mirror(root.left, root.right)

    # def is_mirror(self, node1, node2):
    #     if node1 is None and node2 is None:
    #         return True
    #
    #     elif (node1 is None and node2 is not None) \
    #             and (node1 is not None and node2 is None):
    #         return False
    #
    #     # the case that node is not None
    #     elif node1.val == node2.val:
    #         res1 = self.is_mirror(node1.left, node2.right)
    #         res2 = self.is_mirror(node1.right, node2.left)
    #         return res1 and res2
    #     else:
    #         return False

    def is_mirror(self, node1, node2):
        if node1 is None and node2 is None:
            return True

        if (node1 is None and node2 is not None) and (node1 is not None and node2 is None):
            return False

        # the case that node is not None
        if node1 is not None and node2 is not None:
            if node1.val == node2.val:
                res1 = self.is_mirror(node1.left, node2.right)
                res2 = self.is_mirror(node1.right, node2.left)
                return res1 and res2
        return False
