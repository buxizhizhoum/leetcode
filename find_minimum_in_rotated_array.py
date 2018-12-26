#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:
Input: [3,4,5,1,2]
Output: 1

Example 2:
Input: [4,5,6,7,0,1,2]
Output: 0
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if nums is sorted, no pivot, return first element
        if nums[0] < nums[-1]:
            return nums[0]
        return self.search(nums)

    def search(self, nums):
        if len(nums) < 1:
            return
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2

            # if the element before is larger than after,
            # it means it is at pivot
            if mid + 1 < len(nums) and nums[mid] > nums[mid+1]:
                return nums[mid+1]

            if mid - 1 >= 0 and nums[mid-1] > nums[mid]:
                return nums[mid]

            # still not pass pivot, find on right
            if nums[mid] > nums[0]:
                l = mid + 1

            # passed pivot point, find on left part
            elif nums[mid] < nums[0]:
                r = mid - 1

        return -1


if __name__ == "__main__":
    test_nums = [4, 5, 6, 7, 0, 1, 2]
    test_nums = [2, 1]
    test_nums = [3, 1, 2]
    print(Solution().findMin(test_nums))




