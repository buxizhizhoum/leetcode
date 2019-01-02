#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""
from Queue import LifoQueue


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # return self.kth_smallest(root, k)
        self.k = k
        self.res = None
        self.inorder_traverse(root)
        return self.res

    def kth_smallest(self, root, k):
        if root is None:
            return
        # node count in left sub tree
        count = self.count(root.left)

        # the current node count_left + 1, if current node is kth node, return
        if k == count + 1:
            return root.val

        # if there are enough nodes in left tree, find in left tree
        elif k < count + 1:
            # kth smallest is in left tree
            return self.kth_smallest(root.left, k)
        # if there are not enough nodes in left tree, find in right tree
        else:  # k > count + 1:
            # find k - (count + 1) th node in right tree
            # count + 1 is the node size of left tree + current node
            return self.kth_smallest(root.right, k - (count + 1))

    def count(self, node):
        """
        count the size of tree whose root is node
        :param node:
        :return:
        """
        if node is None:
            return 0

        left = self.count(node.left)
        right = self.count(node.right)

        return left + right + 1

    def inorder_traverse(self, root):
        # todo: it is more clear to use class variable when recursion instead of function wide parameter
        if root is None:
            return

        self.inorder_traverse(root.left)

        self.k -= 1  # if k is used, it is not clear in many recursion
        if self.k == 0:
            self.res = root.val
            return
            # return true and chk may help return advance

        self.inorder_traverse(root.right)

    def inorder_traverse_iter(self, root, k):
        if root is None:
            return

        stack = LifoQueue()
        cur = root
        i = 0
        while not stack.empty() or cur is not None:
            while cur is not None:
                stack.put(cur)
                cur = cur.left

            node = stack.get()
            i += 1
            if i == k:
                return node.val
            cur = node.right


if __name__ == "__main__":
    from tools.construct_binary_tree import Construction

    test_tree = [5, 3, 6, 2, 4, None, None, 1]
    test_root = Construction(test_tree).construct()

    print(Solution().kthSmallest(test_root, 3))
    print(Solution().kthSmallest(test_root, 3))
    print(Solution().inorder_traverse_iter(test_root, 3))





