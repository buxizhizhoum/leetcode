#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
"""


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.tree = self.build_tree(nums)

    def build_tree(self, nums):
        """
        build segment tree according to nums
        :param nums:
        :return: A list stands for segment tree
        """
        # todo: does this bottom up?
        n = len(nums)
        # initialize list used to store tree
        # todo: 4*n ? how 2*n store an complete tree?
        tree = [None for _ in range(2*n)]
        i, j = n, 0
        while i < 2*n:
            tree[i] = nums[j]
            i += 1
            j += 1

        i = n-1
        while i > 0:
            tree[i] = tree[i*2] + tree[i*2 + 1]
            i -= 1

        return tree

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        # convert index in nums to index to tree
        tree_pos = i + len(self.nums)
        self.nums[i] = val  # update original data in array
        self.tree[tree_pos] = val

        while tree_pos > 1:
            left = tree_pos
            right = tree_pos

            if tree_pos % 2 == 0:
                right = tree_pos + 1
            else:
                left = tree_pos - 1

            self.tree[tree_pos//2] = self.tree[left] + self.tree[right]
            tree_pos = tree_pos // 2

    def query(self, i, j):
        length = len(self.nums)
        # convert index of nums to index of tree
        l = i + length
        r = j + length

        res = 0
        while l <= r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 0:
                res += self.tree[r]
                r -= 1

            l //= 2
            r //= 2

        return res

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.query(i, j)


if __name__ == "__main__":
    # Your NumArray object will be instantiated and called as such:
    test_nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(test_nums)
    param_2 = obj.sumRange(0, len(test_nums)-1)
    print(param_2)
    for i in range(len(test_nums)):
        obj.update(i, i)
        param_2 = obj.sumRange(0, len(test_nums) - 1)
        print(param_2, sum(test_nums))


