#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""
from collections import Counter


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.ans(nums)

    def ans(self, nums):
        count = Counter(nums)
        length = len(nums)
        res = []
        for k, v in count.iteritems():
            if v > length // 3:
                res.append(k)

        return res


if __name__ == "__main__":
    test_nums = [1, 1, 1, 3, 3, 2, 2, 2]
    print(Solution().majorityElement(test_nums))


