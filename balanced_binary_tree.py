#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never
differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        left = self.height(root.left)
        right = self.height(root.right)
        if left is False or right is False:
            return False
        if abs(left - right) > 1:
            return False
        else:
            return True

    @classmethod
    def height(cls, node):
        # the height of leaf here is set to 1 instead of 0
        if node is None:
            return 0

        left = cls.height(node.left)
        right = cls.height(node.right)

        # if sub tree of a node is unbalance, the tree is unbalance
        if left is False or right is False:
            return False

        # if the height of left tree and right tree differs more than 1,
        # it is unbalance
        if abs(left - right) > 1:
            return False
        # if it is balance, return the height
        max_h = max(left, right)
        return max_h + 1


if __name__ == "__main__":
    r = TreeNode(6)
    r.left = TreeNode(5)
    r.right = TreeNode(9)

    r.left.left = TreeNode(3)
    r.left.left.left = TreeNode(3)
    # r.left.right = TreeNode(4)

    # r.right.left = TreeNode(7)
    r.right.right = TreeNode(11)
    r.right.right.right = TreeNode(13)

    s = Solution()
    res = s.isBalanced(r)
    print(res)
