#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # delete element from the end of the list
        for index in range((len(nums) - 1), -1, -1):
            if nums[index] == val:
                del nums[index]

        return len(nums)


if __name__ == "__main__":
    # test_list = range(10)
    test_list = [3, 2, 2, 3]
    print Solution().removeElement(test_list, 3)
