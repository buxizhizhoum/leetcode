#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import time
from Queue import Queue


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        queue = Queue()
        queue.put(root)
        queue.put(None)  # None is used to distinguish different level

        res = []
        level = []

        while queue.qsize() != 0:
            node = queue.get()
            if node is not None:
                level.append(node.val)
            else:
                if level:
                    res.append(level)
                    level = []
                    queue.put(None)

            if node is not None:
                if node.left is not None:
                    queue.put(node.left)
                if node.right is not None:
                    queue.put(node.right)

        return res


if __name__ == "__main__":
    from tools.construct_binary_tree import Construction

    values = [3,9,20,None,None,15,7]
    root = Construction(values).construct()

    print(Solution().levelOrder(root))





