#!/usr/bin/python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def create(data):
    head = None
    for item in data:
        if head is None:
            head = ListNode(item)
            cur = head
        else:
            cur.next = ListNode(item)
            cur = cur.next
    return head


if __name__ == "__main__":
    data = range(10)
    linked_list = create(data)
    print(linked_list)

