#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.stack = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        res = []
        while self.stack or root:
            while root is not None:
                self.stack.append(root)
                root = root.left

            tmp = self.stack.pop()
            res.append(tmp.val)
            root = tmp.right
        return res


if __name__ == "__main__":
    # r = TreeNode(6)
    # r.left = TreeNode(5)
    # r.right = TreeNode(9)
    #
    # r.left.left = TreeNode(3)
    # r.left.right = TreeNode(4)
    #
    # r.right.left = TreeNode(7)
    # r.right.right = TreeNode(11)

    r = TreeNode(1)
    r.right = TreeNode(2)
    r.right.left = TreeNode(3)

    s = Solution()
    result = s.inorderTraversal(r)
    print(result)
