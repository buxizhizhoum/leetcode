#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        trick is to delete the node that is next to cur
        make a new node before head
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # a trick, new a node before head
        pre_head = ListNode(None)
        pre_head.next = head
        cur = pre_head

        while cur.next is not None:
            # always delete the next node of cur
            if cur.next.val == val:
                # jump over next node of cur
                cur.next = cur.next.next
                # todo: Attention: after delete node, cur do not move
            else:
                # todo: Attention: cur move to next node only in this case
                cur = cur.next

        return pre_head.next


if __name__ == "__main__":
    from tools.linked_list import LinkedList

    data = [1, 2, 6, 3, 4, 5, 6]
    value = 6
    # data = [1, 1]
    # value = 1

    linked_list = LinkedList(data)
    head1 = linked_list.create()
    linked_list.print_list(head1)

    head_new = Solution().removeElements(head1, value)

    linked_list.print_list(head_new)

