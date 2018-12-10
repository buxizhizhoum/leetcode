#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from Queue import Queue


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.ans(root)

    def ans(self, root):
        if root is None:
            return []
        queue = Queue()
        queue.put((root, 0))
        res = []
        while not queue.empty():
            node, level = queue.get()
            if level == len(res):
                res.append(None)
            res[level] = node.val

            if node.left:
                queue.put((node.left, level + 1))

            if node.right:
                queue.put((node.right, level + 1))
        return res


if __name__ == "__main__":
    from tools.construct_binary_tree import Construction

    data = [3, 9, 20, None, None, 15, 7]
    constructor = Construction(data)
    root = constructor.construct()

    print(Solution().rightSideView(root))

