#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        answer = []
        self.find_subsets(res, answer, nums)
        res.append([])
        return res

    def find_subsets(self, res, answer, nums):
        if len(nums) == 0:
            return

        # when to find combinations of at least k element, optimize is possible
        # for i in range(len(nums) - k + 1), ensure at least k element in nums.
        # 0<=i<len(nums)-k+1 <==> if len(num)>k-1
        # however when find all combinations, not found a way to optimize
        for i in range(len(nums)):
            current_num = nums[i]
            # todo: is there any better method to ensure no dup combinations?
            if sorted(answer + [current_num]) not in res:
                res.append(sorted(answer + [current_num]))
            self.find_subsets(res, answer + [current_num], nums[i+1:])


if __name__ == "__main__":
    test_input = [1, 2, 2]
    print(Solution().subsetsWithDup(test_input))





