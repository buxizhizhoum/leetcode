#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
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
        :rtype: int
        """
        if root is None:
            return 0

        # 寻找路径的3步
        # 第一步表示包含root的路径且和为sum的路径
        res = self.find_path(root, sum)
        # 第二步表示不包含root，在root做子树中寻找和为sum的路径
        res += self.pathSum(root.left, sum)
        # 在右子树中寻找
        res += self.pathSum(root.right, sum)
        return res
        # return self.find_path(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def find_path(self, node, sum):
        """
        find the path that including the given node and sum == given sum
        :param node:
        :param sum:
        :return:
        """
        if node is None:
            return 0

        res = 0
        if node.val == sum:
            res += 1
        res += self.find_path(node.left, sum - node.val)
        res += self.find_path(node.right, sum - node.val)
        return res






