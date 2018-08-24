#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None and n == 1:
            return None
        i, j = 0, n + 1
        node_i, _ = self.nth_node(head, i)
        node_j, tail_flag = self.nth_node(head, j)

        while hasattr(node_j, "next"):
            i += 1
            j += 1
            node_i = node_i.next
            node_j = node_j.next

        if node_i is head:
            if tail_flag:
                head = head.next
            else:
                node_i.next = node_i.next.next
        else:
            node_i.next = node_i.next.next
        return head

    @staticmethod
    def nth_node(head, index):
        j = 0
        res = head
        while j < index and hasattr(res, "next"):
            res = res.next
            j += 1

        tail_flag = True if index - j >= 1 else False

        return res, tail_flag


if __name__ == "__main__":
    test_l_head = None

    for i in range(1, 3):
        if test_l_head is None:
            test_l_head = ListNode(i)
            pointer = test_l_head
        else:
            pointer.next = ListNode(i)
            pointer = pointer.next

    solution = Solution()
    print(solution.removeNthFromEnd(test_l_head, 1))



