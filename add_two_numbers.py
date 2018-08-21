#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # l1_val = l1.val
        # p = l2.val
        res_l = []
        carry = 0
        p = l1
        q = l2
        while p is not None or q is not None or carry != 0:
            p_val = p.val if p is not None else 0
            q_val = q.val if q is not None else 0
            tmp = p_val + q_val + carry

            if tmp >= 10:
                res_l.append(tmp - 10)
                carry = 1
            else:
                res_l.append(tmp)
                carry = 0

            if p is None and q is None:
                break

            p = p.next if p else None
            q = q.next if q else None

        res = self.convert_to_list_node(res_l)
        return res

    @staticmethod
    def convert_to_list_node(l):
        if len(l) == 1:
            return ListNode(l[0])
        res = None
        pointer = None
        for i in range(len(l) - 1):
            new_node = ListNode(l[i + 1])
            if res is None:
                res = ListNode(l[i])
                pointer = res

                pointer.next = new_node
                pointer = pointer.next
            else:
                pointer.next = new_node
                pointer = pointer.next
        return res


if __name__ == "__main__":
    l_a = ListNode(2)
    l_a.next = ListNode(4)
    l_a.next.next = ListNode(3)

    l_b = ListNode(5)
    l_b.next = ListNode(6)
    l_b.next.next = ListNode(9)

    # for i in (2, 4, 3):
    #     if l_a is None:
    #         l_a = ListNode(i)
    #         l_a.next =
    l_a = ListNode(0)
    l_b = ListNode(0)

    s = Solution()
    s.addTwoNumbers(l_a, l_b)

