#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        paths = []
        tmp = []
        self.find_path(root, paths, tmp)
        print(paths)
        res = 0
        for item in paths:
            tmp_str = "".join([str(element) for element in item])
            res += int(tmp_str)
        return res

    def find_path(self, root, paths, tmp):
        if root is None:
            return

        if root.left is None and root.right is None:
            # tmp.append(root.val)
            paths.append(tmp + [root.val])
            return
        else:
            self.find_path(root.left, paths, tmp + [root.val])
            self.find_path(root.right, paths, tmp + [root.val])


if __name__ == "__main__":
    from tools.construct_binary_tree import Construction
    data = [4,9,0,5,1]
    constructor = Construction(data)
    root = constructor.construct()

    Solution().sumNumbers(root)




