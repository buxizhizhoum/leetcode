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

# refer: https://blog.csdn.net/zhang2531/article/details/52424579
# 单链表的实现为：
# 1.使第一个节点为中心点.
# 2.创建2个指针(p,q),p指向头结点,q指向p的下一个节点.
# 3.q开始遍历,如果发现q的值比中心点的值小,则此时p=p->next,并且执行当前p的值和q的值交换,q遍历到链表尾即可.
# 4.把头结点的值和p的值执行交换.此时p节点为中心点,并且完成1轮快排
# 5.使用递归的方法即可完成排序
# not passed, because of time limit exceed.


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
