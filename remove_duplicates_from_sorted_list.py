#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.answer(head)

    def answer(self, head):
        if head is None:
            return head
        cur = head
        while cur.next is not None:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head


if __name__ == "__main__":
    from tools.linked_list import LinkedList

    data = [1, 1, 2, 3, 3]
    linked_list = LinkedList(data)
    head1 = linked_list.create()

    new_head = Solution().deleteDuplicates(head1)

    linked_list.print_list(new_head)


