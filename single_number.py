#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = {}
        for item in nums:
            if counter.get(item) is None:
                counter[item] = 1
            else:
                counter[item] += 1

        for k, v in counter.iteritems():
            if v == 1:
                return k


if __name__ == "__main__":
    test_data = [2,2,1]
    print(Solution().singleNumber(test_data))





