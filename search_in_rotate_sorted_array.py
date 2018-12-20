#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.ans(nums, target)

    def ans(self, nums, target):
        return self._search(nums, target, 0, len(nums) - 1)

    def _search(self, nums, target, start, end):
        if start > end:
            return -1

        mid = start + (end-start)//2
        if nums[mid] == target:
            return mid

        res = -1
        # left part is in order
        if nums[mid] > nums[start]:
            # if target in nums, it should be in left part
            if nums[start] <= target < nums[mid]:
                res = self._search(nums, target, start, mid-1)
        # pivot is in [start, mid)
        # when pivot is in [start, mid), nums[start] > nums[mid]
        else:
            # [start, mid) contains data larger than nums[start] and less than nums[mid]
            if target >= nums[start] or target < nums[mid]:
                res = self._search(nums, target, start, mid-1)

        # right part is in order
        if nums[mid] < nums[end]:
            # if target in nums, it should be in right part
            if nums[mid] < target <= nums[end]:
                res = self._search(nums, target, mid+1, end)
        # pivot is in (mid, end]
        else:
            if target > nums[mid] or target <= nums[end]:
                res = self._search(nums, target, mid+1, end)

        if res != -1:
            return res
        return -1


if __name__ == "__main__":
    test_nums = [4,5,6,7,0,1,2]
    test_target = 0

    test_nums = [3, 1]
    test_target = 1

    print(Solution().search(test_nums, test_target))

