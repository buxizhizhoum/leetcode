#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an array of integers and an integer k, find out whether there are two
distinct indices i and j in the array such that nums[i] = nums[j] and
the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        return self.solve(nums, k)

    def solve(self, nums, k):
        if len(nums) == 0:
            return False

        if k == 0:
            return False

        # initialize buffer set
        buffer_set = set()
        # a window j - i <= k
        for j in range(min(len(nums), k+1)):
            if nums[j] not in buffer_set:
                buffer_set.add(nums[j])
            else:
                return True

        i = 0
        j = k
        while i < len(nums):
            # if j reaches the end of nums
            if j + 1 < len(nums):
                j += 1
                # remove element at left side of window
                buffer_set.remove(nums[i])
                i += 1
                if nums[j] in buffer_set:
                    return True
                else:
                    buffer_set.add(nums[j])
            else:
                return False


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    k = 3
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    print(Solution().containsNearbyDuplicate(nums, k))





