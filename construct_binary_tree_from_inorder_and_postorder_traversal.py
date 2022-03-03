#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
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
    def buildTree(self, inorder, postorder):
        """
        inorder =   [9, 3,  15, 20, 7]
        postorder = [9, 15, 7,  20, 3]
        the root is the last node in postorder, find its index in inorder
        inorder[:index] belong to left tree, inorder[index+1:] belong to right tree

        postorder[:index] belong to left tree, postorder[index:-1] belong to right tree

        left -> root -> right
        left -> right -> root
        after find the root in in order, the left part is at left tree

        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None

        root_val = postorder[-1]
        # index of root node in inorder list
        index = inorder.index(root_val)
        root = TreeNode(root_val)

        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])

        return root


if __name__ == "__main__":
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]

    s = Solution()
    res = s.buildTree(inorder, postorder)
    print(res)






