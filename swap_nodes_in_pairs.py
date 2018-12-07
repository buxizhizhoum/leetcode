#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.ans_1(head)

    def ans(self, head):
        if head is None or head.next is None:
            return head

        dummy_head = ListNode(None)
        dummy_head.next = head

        pre = dummy_head
        node1 = pre.next
        while node1 is not None and node1.next is not None:
            node2 = node1.next
            node_next = node2.next

            node2.next = node1
            pre.next = node2
            node1.next = node_next

            pre = node1
            node1 = pre.next
            linked_list.print_list(dummy_head.next)
        return dummy_head.next

    def ans_1(self, head):
        if head is None or head.next is None:
            return head

        dummy_head = ListNode(None)
        dummy_head.next = head

        pre = dummy_head
        while pre.next is not None and pre.next.next is not None:
            node1 = pre.next
            node2 = node1.next
            node_next = node2.next

            node2.next = node1
            pre.next = node2
            node1.next = node_next

            pre = node1

        return dummy_head.next


if __name__ == "__main__":
    from tools.linked_list import LinkedList

    data = range(3)
    linked_list = LinkedList(data)
    head1 = linked_list.create()
    linked_list.print_list(head1)

    head_new = Solution().swapPairs(head1)

    linked_list.print_list(head_new)

