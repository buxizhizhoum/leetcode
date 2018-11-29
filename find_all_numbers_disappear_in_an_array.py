#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""


# 哪个元素出现了，第几个位置的数据就设置为负值，
# 通过某个位置正负表示这个位置对应的索引数据是否出现


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     index = abs(nums[i]) - 1
        #     nums[index] = -1 * nums[index] if nums[index] > 0 else nums[index]

        # modify element whose location could be specified by item to negative
        for item in nums:
            index = abs(item) - 1
            nums[index] = -abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


if __name__ == "__main__":
    test_input = [2, 2]
    print(Solution().findDisappearedNumbers(test_input))




