#!/usr/bin/python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = None
        pointer_1 = l1
        pointer_2 = l2

        while pointer_1 is not None and pointer_2 is not None:
            if pointer_1.val <= pointer_2.val:
                if res is None:
                    res = ListNode(pointer_1.val)
                    header = res
                else:
                    header.next = ListNode(pointer_1.val)
                    header = header.next
                pointer_1 = pointer_1.next
            else:
                if res is None:
                    res = ListNode(pointer_2.val)
                    header = res
                else:
                    header.next = ListNode(pointer_2.val)
                    header = header.next
                pointer_2 = pointer_2.next

        while pointer_1 is not None:
            if res is None:
                res = ListNode(pointer_1.val)
                header = res
            else:
                header.next = ListNode(pointer_1.val)
                header = header.next
            pointer_1 = pointer_1.next

        while pointer_2 is not None:
            if res is None:
                res = ListNode(pointer_2.val)
                header = res
            else:
                header.next = ListNode(pointer_2.val)
                header = header.next
            pointer_2 = pointer_2.next

        return res


if __name__ == "__main__":
    # test_l1 = [1, 3, 5]
    # test_l2 = [2, 4, 6]
    # test_l1 = [1, 2, 4]
    # test_l2 = [1, 3, 4]
    # test_l1 = ListNode(1)
    # test_l1.next = ListNode(2)
    # test_l1.next.next = ListNode(4)
    #
    # test_l2 = ListNode(1)
    # test_l2.next = ListNode(3)
    # test_l2.next.next = ListNode(4)
    test_l1 = None
    test_l2 = ListNode(1)
    print(Solution().mergeTwoLists(test_l1, test_l2))
