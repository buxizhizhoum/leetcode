#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.binary_search(nums, target)

    def binary_search(self, nums, target):
        l = 0
        r = len(nums) - 1  # [l, r]

        index = -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                index = mid
                break
                # return mid

            elif nums[mid] < target:
                l = mid + 1
            else:  # nums[mid] > target
                r = mid - 1

        # return -1
        # return self.search_around(nums, index, target)
        return self.search_around_1(nums, index, target)

    def search_around(self, nums, index, target):
        """
        linear search
        :param nums:
        :param index:
        :param target:
        :return:
        """
        if index == -1:
            return [-1, -1]

        l = index
        r = index

        while l > 0 and r < len(nums)-1:
            while nums[l-1] == target:
                l -= 1

            while nums[r+1] == target:
                r += 1

            break

        return [l, r]

    def search_around_1(self, nums, index, target):
        """
        binary search
        :param nums:
        :param index:
        :param target:
        :return:
        """
        if index == -1:
            return [-1, -1]

        l_start = 0
        l_end = index  # -1 or not

        r_end = len(nums) - 1
        r_start = index

        first_index = index
        last_index = index
        # binary search left part to find first index of target
        # when ==, means there is only one element in list
        while l_start <= l_end:
            l_mid = l_start + (l_end - l_start) // 2
            if nums[l_mid] == target:
                # do not stop, search forward continue
                first_index = l_mid
                l_end = l_mid - 1

            elif nums[l_mid] < target:
                l_start = l_mid + 1
            else:
                # in fact it is impossible to go to this branch
                l_end = l_mid - 1  # -1 or not

        # binary search right part to find last index of target
        while r_start <= r_end:
            r_mid = r_start + (r_end - r_start) // 2
            if nums[r_mid] == target:
                last_index = r_mid
                r_start = r_mid + 1

            elif nums[r_mid] < target:
                r_start = r_mid + 1

            else:
                r_end = r_mid - 1

        return [first_index, last_index]


if __name__ == "__main__":
    test_data = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]
    target = 2
    print(Solution().searchRange(test_data, target))




