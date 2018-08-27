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
    def __init__(self):
        # self.pre_val = float("-inf")
        self.pre_val = None
        self.flag = True

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.inorder(root)
        return self.flag

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        if self.pre_val is not None and self.pre_val >= node.val:
            self.flag = False

        self.pre_val = node.val
        self.inorder(node.right)


if __name__ == "__main__":
    # r = TreeNode(10)
    # r.left = TreeNode(5)
    # r.right = TreeNode(15)
    #
    # # r.left.left = TreeNode(3)
    # # r.left.right = TreeNode(4)
    #
    # # r.right.left = TreeNode(6)
    # r.right.left = TreeNode(11)
    # r.right.right = TreeNode(20)

    r = TreeNode(1)
    r.left = TreeNode(1)
    # r.right = TreeNode(2)
    # r.right.left = TreeNode(3)

    s = Solution()
    result = s.isValidBST(r)
    print(result)
