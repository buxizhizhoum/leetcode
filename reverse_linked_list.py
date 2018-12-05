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
    from tools.create_linked_list import create
    test_linked_list = create(range(1, 6))

    print(Solution().reverseList(test_linked_list))


