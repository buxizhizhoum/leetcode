#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""
from collections import Counter


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.ans(nums)

    def ans(self, nums):
        counter = Counter(nums)
        length = len(nums)
        for k, v in counter.iteritems():
            if v > length // 2:
                return k
        return None


if __name__ == "__main__":
    test_nums = [3, 2, 3]
    print(Solution().majorityElement(test_nums))


