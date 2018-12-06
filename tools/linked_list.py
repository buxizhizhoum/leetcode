#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList(object):
    def __init__(self, data):
        self.data = data

    def create(self):
        if not self.data:
            return None
        head = ListNode(self.data[0])
        cur = head
        for item in self.data[1:]:
            cur.next = ListNode(item)
            cur = cur.next
        return head

    def print_list(self, head):
        cur = head
        while cur is not None:
            print(cur.val, end="->")
            cur = cur.next
        print("NULL")


if __name__ == "__main__":
    data = range(10)
    linked_list = LinkedList(data)
    head = linked_list.create()
    linked_list.print_list(head)

