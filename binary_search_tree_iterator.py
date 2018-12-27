#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Example:
            7
          /  \
         3   15
            /  \
           9    20

BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false


Note:
next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
"""
from Queue import LifoQueue


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    """
    the smallest value of current node is at leftest of current node,
    in order to reach smallest value, we have to search to leftest, however
    after return smallest value, we have to return to its father node, since
    there is no pointer to a node's father, we have to cache a node's father
    node when searching, this is why stack is used.

    when a node is pop from stack, if the node have a right node the next smallest
    node is at right sub tree, the right node and it left node, and left node's left node
    should be put to stack and waiting for pop
    """
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = LifoQueue()
        self.push(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if not self.stack.empty():
            node = self.stack.get()
            # every time to pop a node from stack,
            # push right node and its leftest node to stack
            self.push(node.right)
            return node.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if not self.stack.empty():
            return True
        return False

    def push(self, node):
        """
        push node and its left node to stack recursively
        :param node:
        :return:
        """
        if node is None:
            return
        self.stack.put(node)
        self.push(node.left)


if __name__ == "__main__":
    # Your BSTIterator object will be instantiated and called as such:
    from tools.construct_binary_tree import Construction

    tree = [7, 3, 15, None, None, 9, 20]
    root = Construction(tree).construct()

    obj = BSTIterator(root)
    for i in range(5):
        param_1 = obj.next()
        param_2 = obj.hasNext()
        print(param_1)
        print(param_2)



