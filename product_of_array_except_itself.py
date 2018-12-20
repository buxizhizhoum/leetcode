#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an array nums of n integers where n > 1,  return an array output such
that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for the purpose of space complexity analysis.)
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.ans(nums)

    def ans(self, nums):
        cache_1 = []
        cache_1.append(1)  # the first element is 1
        for index, item in enumerate(nums[1:], start=1):
            tmp = cache_1[index-1] * nums[index-1]
            cache_1.append(tmp)

        cache_2 = [1 for _ in nums]
        # from end to beginning
        for i in range(len(nums)-2, -1, -1):
            tmp = cache_2[i+1] * nums[i+1]
            cache_2[i] = tmp

        res = []
        for i in range(len(nums)):
            tmp = cache_1[i] * cache_2[i]
            res.append(tmp)

        return res


if __name__ == "__main__":
    test_data = [1,2,3,4]
    print(Solution().ans(test_data))

