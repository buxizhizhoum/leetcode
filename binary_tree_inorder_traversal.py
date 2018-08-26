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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is not None:
            res = self.traverse_node(root)
        return res

    @classmethod
    def traverse_node(cls, node):
        res = []
        if node is None:
            return []
        # if node.left is None and node.right is None:
        #     return [node.val]

        # if node.left is not None:
        left_val = cls.traverse_node(node.left)
        res.extend(left_val)

        res.append(node.val)

        # if node.right is not None:
        right_val = cls.traverse_node(node.right)
        res.extend(right_val)

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
