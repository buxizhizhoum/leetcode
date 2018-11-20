#!/usr/bin/python
# -*- coding: utf-8 -*-
from Queue import Queue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Construction(object):
    def __init__(self, values):
        self.values = values
        self.length = len(values)
        self.queue = Queue()

    def construct(self):
        """
        每次循环从队列拿出有一个节点，同时将拿出的这个节点的左右子节点放入队列，
        创建树是一层一层向下的。
        队列中保存当前节点同一层后面的其它节点以及当前节点和前面的所有节点下一层的左右子节点
        :return:
        """
        if self.length == 0:
            return

        root = TreeNode(self.values[0])
        i = 0
        while i < self.length:

            if i == 0:
                node = root
            else:
                if self.queue.empty():
                    break
                node = self.queue.get()
            # left index 2*i + 1, right index 2*i + 2
            left_index = 2 * i + 1
            right_index = 2 * i + 2

            if left_index < self.length:
                left_val = self.values[left_index]
                if left_val is not None:
                    tmp_node = TreeNode(left_val)
                    self.queue.put(tmp_node)
                    node.left = tmp_node

            if right_index < self.length:
                right_val = self.values[right_index]
                if right_val is not None:
                    tmp_node = TreeNode(right_val)
                    self.queue.put(tmp_node)
                    node.right = tmp_node

            i += 1
        return root


if __name__ == "__main__":
    data = range(10)
    # [5,4,8,11,null,13,4,7,2,null,null,5,1]
    data = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    constructor = Construction(data)
    root = constructor.construct()
    print(root)


