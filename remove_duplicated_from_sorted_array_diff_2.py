#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return

        cur_val = nums[-1]
        cur_count = 0
        for i in range(len(nums) - 1, -1, -1):
            if cur_val == nums[i]:
                cur_count += 1
                if cur_count > 2:
                    del (nums[i])
            else:
                cur_val = nums[i]
                cur_count = 1


if __name__ == "__main__":
    test_input = [0,0,1,1,1,1,2,3,3]
    test_input = []
    Solution().removeDuplicates(test_input)
    print(test_input)


