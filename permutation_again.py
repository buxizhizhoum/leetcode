#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        answer = []
        length = len(nums)
        self.find_permute(nums, res, answer, length)
        return res

    def find_permute(self, nums, res, answer, length):
        # if len(nums) == 0 is enough.
        if len(nums) == 0 and len(answer) == length:
            res.append(answer)
            return

        for i in range(0,  len(nums)):
            current_num = nums[i]
            # nums[:i] + nums[i+1:] is the smaller list after num[i] is removed
            self.find_permute(nums[:i] + nums[i+1:], res, [current_num] + answer, length)


if __name__ == "__main__":
    test_nums = [1, 2, 3]
    print(Solution().permute(test_nums))





