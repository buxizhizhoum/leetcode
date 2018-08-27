#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_valid(root)

    @classmethod
    def is_valid(cls, node, floor=float("-inf"), ceiling=float("inf")):
        if node is None:
            return True

        if node.left is not None:
            if floor < node.left.val < node.val:
                # when check the left sub tree of a node,
                # the floor is the floor of the nodes so far,
                # the ceiling is the value of current node

                # ceiling is needed when to check left sub tree, all nodes of
                # left sub tree should be less than a value
                left = cls.is_valid(node.left, floor=floor, ceiling=node.val)
            else:
                left = False
        else:
            left = True

        if node.right is not None:
            if node.val < node.right.val < ceiling:
                # floor is need when to check right sub tree, since all nodes
                # of right sub tree should be larger than a value
                right = cls.is_valid(node.right, floor=node.val, ceiling=ceiling)
            else:
                right = False
        else:
            right = True

        return left and right


if __name__ == "__main__":
    r = TreeNode(10)
    r.left = TreeNode(5)
    r.right = TreeNode(15)

    # r.left.left = TreeNode(3)
    # r.left.right = TreeNode(4)

    r.right.left = TreeNode(6)
    r.right.right = TreeNode(20)

    # r = TreeNode(1)
    # r.right = TreeNode(2)
    # r.right.left = TreeNode(3)

    s = Solution()
    result = s.isValidBST(r)
    print(result)
