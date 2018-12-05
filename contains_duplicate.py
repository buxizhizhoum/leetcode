#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # return self.set_ans(nums)
        return self.set_ans_1(nums)

    def set_ans(self, nums):
        return len(nums) != len(set(nums))

    def set_ans_1(self, nums):
        buffer_set = set()
        for num in nums:
            if num not in buffer_set:
                buffer_set.add(num)
            else:
                return True
        return False


if __name__ == "__main__":
    test_input = [1, 1, 2, 2]
    print(Solution().containsDuplicate(test_input))

