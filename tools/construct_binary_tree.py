#!/usr/bin/python
# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Construction(object):
    def __init__(self, values):
        self.values = values
        self.length = len(values)

    def construct(self):
        if self.length == 0:
            return

        root = TreeNode(self.values[0])
        self._construct(root, 0)

        return root

    def _construct(self, node, i):
        # left index 2*i + 1, right index 2*i + 2
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < self.length and node.val is not None:
            left_value = self.values[left_index]
            node.left = TreeNode(left_value)
            self._construct(node.left, left_index)

        if right_index < self.length and node.val is not None:
            right_value = self.values[right_index]
            node.right = TreeNode(right_value)
            self._construct(node.right, right_index)

        return node


if __name__ == "__main__":
    data = range(10)
    constructor = Construction(data)
    root = constructor.construct()
    print(root)


