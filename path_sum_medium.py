#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        res = []
        tmp = []
        self.find_path(root, res, tmp, sum)
        return res

    def find_path(self, node, res, tmp, sum_):
        # node is None is the stop condition
        if node is None:
            return
        # if is leaf and sum == given sum
        if node.left is None and node.right is None:
            if node.val == sum_:
                tmp.append(node.val)
                # append to res only when the sum is right
                res.append(tmp)
                return
        # todo: think again, append and + in function call is different
        # tmp.append(node.val)
        self.find_path(node.left, res, tmp + [node.val], sum_ - node.val)
        self.find_path(node.right, res, tmp + [node.val], sum_ - node.val)


if __name__ == "__main__":
    from tools.construct_binary_tree import Construction

    data = [5, 4, 8, 11, 1, 13, 4, 7, 2, 11, 19, 5, 1]
    constructor = Construction(data)
    root = constructor.construct()
    Solution().pathSum(root, 22)





