#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
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
        return self.my_ans(head)
        # return self.web_ans(head)

    def my_ans(self, head):
        dummy_head = ListNode(None)
        cur = dummy_head
        cur.next = head

        while cur.next is not None:
            if cur.next.next and cur.next.val == cur.next.next.val:
                while cur.next and cur.next.next and cur.next.val == cur.next.next.val:
                    cur.next = cur.next.next
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy_head.next

    def web_ans(self, head):
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head

        while cur.next:
            if cur.val == cur.next.val:
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur = cur.next
                pre.next = cur
            else:
                pre = pre.next
                cur = cur.next
        return dummy.next


if __name__ == "__main__":
    from tools.linked_list import LinkedList

    data = [1, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10]
    linked_list = LinkedList(data)
    head1 = linked_list.create()
    linked_list.print_list(head1)

    head_new = Solution().deleteDuplicates(head1)

    linked_list.print_list(head_new)

