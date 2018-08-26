#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.flatten_node(root)

    @classmethod
    def flatten_node(cls, node):
        if node is None:
            return
        if node.left is not None:
            tmp = node.right
            node.right = node.left
            node.left = None
            cls.flatten_node(node.right)
            while node.right is not None:
                node = node.right
            node.right = tmp
        cls.flatten_node(node.right)


if __name__ == "__main__":
    r = TreeNode(6)
    r.left = TreeNode(5)
    r.right = TreeNode(9)

    r.left.left = TreeNode(3)
    r.left.left.left = TreeNode(1)
    # r.left.right = TreeNode(4)

    # r.right.left = TreeNode(7)
    r.right.right = TreeNode(11)
    r.right.right.right = TreeNode(13)

    s = Solution()
    res = s.flatten(r)
    print(res)



