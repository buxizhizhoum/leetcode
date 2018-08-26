#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a binary tree, return the bottom-up level order traversal of its
nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = []
        res = []
        root_level = (root, 0)  # the node and its level
        queue.append(root_level)
        while queue:
            node, level = queue.pop(0)
            if node:
                res.append((node.val, level))
            tmp_nodes = self.traverse_node(node, level)
            queue.extend(tmp_nodes)
        return self.convert(res)

    @staticmethod
    def traverse_node(node, level):
        res = []
        if node is None:
            return res

        res.append((node.left, level + 1))
        res.append((node.right, level + 1))
        return res

    @staticmethod
    def convert(nodes_level):
        res_d = {}
        res = []
        if not nodes_level:
            return res
        # put nodes of different level under different key
        for node, level in nodes_level:
            if level not in res_d.keys():
                res_d[level] = [node]
            else:
                res_d[level].append(node)

        for k, v in res_d.items():
            res.append(v)

        res.reverse()
        return res


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    s = Solution()
    result = s.levelOrderBottom(root)
    print(result)
