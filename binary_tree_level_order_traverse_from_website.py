#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import deque


class Solution:
    def levelOrder(self, root):
        if not root: return []
        queue, res = deque([root]), []

        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            res.append(cur_level)
        return res


if __name__ == "__main__":
    from tools.construct_binary_tree import Construction

    values = [3,9,20,None,None,15,7]
    root = Construction(values).construct()

    print(Solution().levelOrder(root))








