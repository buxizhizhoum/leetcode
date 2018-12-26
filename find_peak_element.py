#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.
"""


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self.linear_scan(nums)
        return self.binary_search(nums)

    def linear_scan(self, nums):
        if not nums:
            return None

        if len(nums) == 1:
            return 0

        elif len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1

        for index, number in enumerate(nums):
            if index == 1:
                if nums[index] < nums[index-1]:
                    return index-1
            if index == len(nums) - 2:
                if nums[index] < nums[index + 1]:
                    return index + 1

            if index-1 >= 0 and index+1 < len(nums) and nums[index-1] < number and number > nums[index+1]:
                return index
        return None

    def binary_search(self, nums):
        if not nums:
            return None

        if len(nums) == 1:
            return 0

        elif len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            # stop condition
            if mid - 1 >= 0 and mid+1 < len(nums):
                if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                    return mid
            elif mid-1 >= 0:
                if nums[mid-1] < nums[mid]:
                    return mid
            elif mid+1 < len(nums):
                if nums[mid] > nums[mid+1]:
                    return mid

            # on ascending side, peak is at right
            if mid+1 < len(nums) and nums[mid] < nums[mid+1]:
                l = mid + 1
            # on descending side, peak is at left
            elif mid+1 < len(nums) and nums[mid] > nums[mid+1]:
                r = mid - 1

        return l

if __name__ == "__main__":
    test_nums = [1,2,1,3,5,6,4]
    # test_nums = [2, 1]
    # test_nums = [3, 2, 1]
    test_nums = [1,2,3,1]
    # test_nums = [1,2,1]
    # test_nums = [1,2,3]
    print(Solution().findPeakElement(test_nums))



