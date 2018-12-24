#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.ans(nums, target)

    def ans(self, nums, target):
        nums.sort()
        difference = float("inf")
        for i, item in enumerate(nums[:-2]):
            l, r = i + 1, len(nums) - 1
            while l < r:
                num_sum = item + nums[l] + nums[r]
                if num_sum == target:
                    return target

                elif num_sum < target:
                    tmp = target - num_sum
                    # update to closer difference
                    if tmp < difference:
                        difference = tmp
                        res = target - tmp

                    l += 1

                else:  # item + nums[i] + nums[r] > target
                    tmp = target - num_sum
                    # update to a closer difference
                    if abs(tmp) < difference:
                        difference = abs(tmp)
                        res = target + abs(tmp)

                    r -= 1

        return res


if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1

    nums = [-3, -2, -5, 3, -4]
    target = -1
    print(Solution().threeSumClosest(nums, target))



