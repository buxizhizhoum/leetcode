#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        return self.ans_pq(lists)

    def ans_pq(self, lists):
        from Queue import PriorityQueue

        pq = PriorityQueue()
        for single_list in lists:
            cur = single_list
            while cur is not None:
                pq.put((cur.val, cur))
                cur = cur.next

        head = None
        cur = head
        while not pq.empty():
            _, node = pq.get()
            if head is None:
                head = node
                cur = head
            else:
                cur.next = node
                cur = cur.next
        if cur is not None:
            cur.next = None
        return head


if __name__ == "__main__":
    from tools.linked_list import LinkedList

    l1 = [1,2,3]
    l2 = [1,3,5]
    l3 = [2,3,9]

    l1 = [1, 2, 2]
    l2 = [1, 1, 2]

    linked_list_1 = LinkedList(l1)
    linked_list_2 = LinkedList(l2)
    # linked_list_3 = LinkedList(l3)

    head_1 = linked_list_1.create()
    head_2 = linked_list_2.create()
    # head_3 = linked_list_3.create()

    # test_lists = [head_1, head_2, head_3]
    test_lists = [head_1, head_2]

    head_new = Solution().mergeKLists(test_lists)

    linked_list_1.print_list(head_new)



