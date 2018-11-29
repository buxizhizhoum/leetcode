#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums

        first_zero = 0
        positive_after_zero = 0

        while positive_after_zero < len(nums) and first_zero < len(nums):

            if nums[first_zero] != 0:
                first_zero += 1
                continue

            if nums[positive_after_zero] == 0:
                positive_after_zero += 1
                continue

            if first_zero < positive_after_zero:
                nums[first_zero], nums[positive_after_zero] = nums[positive_after_zero], nums[first_zero]
                first_zero += 1
                positive_after_zero += 1
            else:
                positive_after_zero += 1


if __name__ == "__main__":
    test_input = [0,1,0,3,12]
    test_input = [1]
    test_input = [1,0,1]
    # test_input = [1,0]
    Solution().moveZeroes(test_input)
    print(test_input)






