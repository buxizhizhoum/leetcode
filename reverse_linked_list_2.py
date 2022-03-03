from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}"


class Solution:
    def reverse(self, left, right):
        """reverse linked list between node left and right"""
        if left is None:
            return left, right
        # end = right.next
        pre = right.next
        cur = left
        # while cur != end:
        while pre != right:
            next_node = cur.next
            cur.next = pre

            pre = cur
            cur = next_node

        return right, left

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pre = ListNode(0)
        pre.next = head
        cur = head

        left_node = head
        right_node = head
        for i in range(1, right+1):
            if i == left - 1:
                pre = cur
            elif i == left:
                left_node = cur
            if i == right:
                right_node = cur
            cur = cur.next

        left_node, right_node = self.reverse(left_node, right_node)
        pre.next = left_node
        return head if left > 1 else left_node


if __name__ == "__main__":
    from tools.linked_list import LinkedList
    # linked_list = LinkedList(range(1, 6))
    linked_list = LinkedList([3, 5])
    test_head = linked_list.create()

    linked_list.print_list(test_head)
    # reversed_head = Solution().reverseBetween(test_head, 2, 4)
    reversed_head = Solution().reverseBetween(test_head, 2, 2)
    linked_list.print_list(reversed_head)

