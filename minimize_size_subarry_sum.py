#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution,
try coding another solution of which the time complexity is O(n log n).
"""


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = 0

        res = float("inf")
        sum_ = 0
        while start < len(nums):
            if sum_ < s:
                if end < len(nums):
                    sum_ += nums[end]
                    end += 1
                else:
                    # if end return to right and still less than s,
                    # there is no way to increase, the only way is to break
                    break
            else:
                sum_ -= nums[start]
                start += 1

            if sum_ >= s:
                res = min(res, end - start)

        if res == float("inf"):
            return 0
        return res

    def version_1(self, s, nums):
        start = 0
        end = 0

        res = float("inf")
        # sum_ = nums[start]
        sum_ = 0
        while start < len(nums):
            if sum_ < s:
                if end < len(nums):
                    sum_ += nums[end]
                    end += 1
                else:
                    break
            else:
                res = min(res, end - start)
                sum_ -= nums[start]
                start += 1

        if res == float("inf"):
            return 0
        return res


if __name__ == "__main__":
    test_input = [2,3,1,2,4,3]
    test_s = 7
    # test_input = [1,1]
    # test_s = 3

    print(Solution().minSubArrayLen(test_s, test_input))






