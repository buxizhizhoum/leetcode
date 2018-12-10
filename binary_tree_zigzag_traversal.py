#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from Queue import Queue


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        return self.reorder(self.ans(root))

    def ans(self, root):
        if root is None:
            return
        queue = Queue()
        queue.put((root, 0))
        res = []
        while not queue.empty():
            node, level = queue.get()

            if level == len(res):
                res.append([])
            res[level].append(node.val)

            if node.left:
                queue.put((node.left, level + 1))
            if node.right:
                queue.put((node.right, level + 1))

        return res

    def reorder(self, res):
        if not res:
            return []
        for level in range(len(res)):
            if level % 2 == 1:
                res[level] = res[level][::-1]

        return res


if __name__ == "__main__":
    from tools.construct_binary_tree import Construction

    data = [3, 9, 20, None, None, 15, 7]
    constructor = Construction(data)
    root = constructor.construct()

    print(Solution().zigzagLevelOrder(root))

