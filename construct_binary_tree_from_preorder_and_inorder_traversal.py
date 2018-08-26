#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return
        index = inorder.index(preorder[0])
        root = TreeNode(inorder[index])

        inorder_left = inorder[:index]
        inorder_right = inorder[index + 1:]
        preorder.pop(0)

        root.left = self.buildTree(preorder, inorder_left)
        root.right = self.buildTree(preorder, inorder_right)
        return root


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    s = Solution()
    res = s.buildTree(preorder, inorder)
    print(res)


