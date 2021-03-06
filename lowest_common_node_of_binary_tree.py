#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
             according to the LCA definition.
Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""
from Queue import Queue


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.recursion(root, p, q)

    def recursion(self, root, p, q):
        if root is None:
            return

        if root == p or root == q:
        # if root.val == p or root.val == q:
            return root

        if root != p and root != q:
        # if root.val != p and root.val != q:
            left = self.recursion(root.left, p, q)
            right = self.recursion(root.right, p, q)
            if left and right:
                return root
            else:
                return left or right

    def iteration(self, root, p, q):
        # todo: could union find be used? seems not.
        queue = Queue()
        parents = {root: None}

        queue.put(root)
        # todo: queue empty necessary or not?
        # if p and q is tree node in tree, there will finally in parents,
        # so queue.empty is unnecessary.
        while p not in parents or q not in parents:
        # while not queue.empty() and (p not in parents or q not in parents):
            node = queue.get()

            if node.left is not None:
                parents[node.left] = node
                queue.put(node.left)

            if node.right is not None:
                parents[node.right] = node
                queue.put(node.right)

        ancestor = set()
        p_cur = p
        while p_cur is not None:
            ancestor.add(p_cur)
            p_cur = parents[p_cur]

        cur = q
        while cur not in ancestor:
            cur = parents[cur]

        return cur


if __name__ == "__main__":
    from tools.construct_binary_tree import Construction

    test_tree = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]

    test_root = Construction(test_tree).construct()

    # print(Solution().lowestCommonAncestor(test_root, 5, 1).val)
    print(Solution().iteration(test_root, TreeNode(5), TreeNode(1)).val)

