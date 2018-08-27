#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        end = self.end(head)
        self.quick_sort(head, end)
        return head

    @classmethod
    def quick_sort(cls, head, end):
        if head and end and head is not end:
            partition_node = cls.partition(head, end)
            cls.quick_sort(head, partition_node)
            cls.quick_sort(partition_node.next, end)

    @classmethod
    def partition(cls, head, end):
        if head is None:
            return None

        mid_val = head.val
        slow = head
        fast = head.next

        # the nodes before slow is less than mid point
        # the nodes between slow and fast is larger than mid point
        while fast is not end.next:
            if fast.val < mid_val:
                slow = slow.next
                # swap the val of slow and fast
                fast.val, slow.val = slow.val, fast.val
            fast = fast.next
        slow.val, head.val = head.val, slow.val
        return slow

    @staticmethod
    def end(head):
        if head is None:
            return head

        res = head
        while res.next is not None:
            res = res.next

        return res


if __name__ == "__main__":
    # l = ListNode(5)
    # l.next = ListNode(3)
    # l.next.next = ListNode(9)
    # l.next.next.next = ListNode(2)

    l = ListNode(4)
    l.next = ListNode(2)
    l.next.next = ListNode(1)
    l.next.next.next = ListNode(3)

    s = Solution()
    s.sortList(l)
    print(l)
