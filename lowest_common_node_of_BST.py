#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself
             according to the LCA definition.
Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.
"""


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
        if root is None:
            return None

        if p is None or q is None:
            return None

        # if (root.val == p.val and root.val < q.val) or (root.val == p.val and root.val > q.val):
        #     return root
        # if (root.val == q.val and root.val > p.val) or (root.val == q.val and root.val < p.val):
        #     return root
        if root.val == p.val or root.val == q.val:
            return root
        # root.val between p and q
        if p.val < root.val < q.val or q.val < root.val < p.val:
            return root

        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > q.val and root.val > p.val:
            return self.lowestCommonAncestor(root.left, p, q)


if __name__ == "__main__":
    from tools.construct_binary_tree import Construction
    data = [6,2,8,0,4,7,9,None,None,3,5]
    p_val, q_val = 2, 4
    data = [2,1]
    p_val, q_val = 1, 2

    constructor = Construction(data)
    root = constructor.construct()

    p_node = TreeNode(p_val)
    q_node = TreeNode(q_val)
    res = Solution().lowestCommonAncestor(root, p_node, q_node)
    print(res)



