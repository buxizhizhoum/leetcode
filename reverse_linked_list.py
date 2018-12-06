#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        pre = None
        cur = head
        while cur is not None:
            next = cur.next

            # cur.next point to pre
            cur.next = pre
            # pre point to cur
            pre = cur
            # cur point to next
            cur = next

            # the next loop, next point to cur.next

        return pre


if __name__ == "__main__":
    from tools.linked_list import LinkedList
    linked_list = LinkedList(range(1, 6))
    test_head = linked_list.create()

    linked_list.print_list(test_head)
    reversed_head = Solution().reverseList(test_head)
    linked_list.print_list(reversed_head)
