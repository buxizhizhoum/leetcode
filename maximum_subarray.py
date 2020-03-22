#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution
using the divide and conquer approach, which is more subtle.
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        if len(nums) == 1:
            return nums[0]

        res = nums[0]
        # cur_sum = nums[0]
        max_sum = res
        for i in range(1, len(nums)):
            # accumulate is better than start from current
            if res + nums[i] >= nums[i]:
                res += nums[i]
            # start from current point
            else:
                res = nums[i]

            max_sum = max(res, max_sum)
        return max_sum


if __name__ == "__main__":
    test_data = [-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    print solution.maxSubArray(test_data)








