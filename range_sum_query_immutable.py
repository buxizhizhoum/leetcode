#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.memo = self.cache()
        self.memo_sentinel = self.cache_sentinel()

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # return self.brute_force(i, j)
        # return self.calculate(i, j)
        return self.calculate_sentinel(i, j)

    def brute_force(self, i, j):
        return sum(self.nums[i: j+1])

    def cache(self):
        """
        cache sum of [0, i] to memo[i]
        :return:
        """
        memo = [0 for _ in range(len(self.nums))]

        for index, number in enumerate(self.nums):
            if index == 0:
                memo[index] = number
            else:
                memo[index] = memo[index-1] + number
        return memo

    def calculate(self, i, j):
        if i <= 0:
            # sum of element before index 0 is 0, boundary condition
            sum_before_i = 0
        else:
            sum_before_i = self.memo[i-1]

        res = self.memo[j] - sum_before_i
        return res

    def cache_sentinel(self):
        """
        cache sum of [0, i+1] to memo[i]
        :return:
        """
        # length of memo is n + 1, first element is sentinel, stands for sum(num[:0])
        memo = [0 for _ in range(len(self.nums) + 1)]

        for index, number in enumerate(self.nums, start=1):
            memo[index] = memo[index-1] + number
        return memo

    def calculate_sentinel(self, i, j):
        res = self.memo_sentinel[j+1] - self.memo_sentinel[i]
        return res


if __name__ == "__main__":
    # Your NumArray object will be instantiated and called as such:
    test_nums = [-2, 0, 3, -5, 2, -1]
    i, j = 0, 2
    i, j = 2, 5
    i, j = 0, 5
    obj = NumArray(test_nums)
    param_1 = obj.sumRange(i, j)
    print(param_1)



