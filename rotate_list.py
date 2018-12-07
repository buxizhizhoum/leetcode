#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        return self.my_ans(head, k)

    def my_ans(self, head, k):
        length = self.length(head)
        if length <= 1:
            return head

        # calculate the really rotate steps needed
        if k >= length:
            # if rotate step is larger than length, recalculate it.
            k = k % length

        if k == 0:
            return head

        # modify linked list to a cycle list
        self.cycle(head)
        # how many nodes to forward in cycle list
        step = length - k
        cur = head
        for _ in range(step - 1):
            cur = cur.next
        head = cur.next
        cur.next = None
        return head


    def cycle(self, head):
        """
        modify a linked list to a cycle list in place
        :param head:
        :return:
        """
        cur = head
        while cur.next is not None:
            cur = cur.next
        # point cur.next to head to make it a cycle list
        cur.next = head

    def length(self, head):
        cur = head
        length = 0
        while cur is not None:
            length += 1
            cur = cur.next
        return length


if __name__ == "__main__":
    from tools.linked_list import LinkedList

    data = range(1, 6)
    linked_list = LinkedList(data)

    head1 = linked_list.create()
    linked_list.print_list(head1)

    head_new = Solution().rotateRight(head1, 111)

    linked_list.print_list(head_new)




