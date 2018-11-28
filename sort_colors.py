#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # self.count_sort(nums)
        self.quick_sort_3_way_1(nums)

    def count_sort(self, nums):
        if not nums:
            return
        cache = [0 for _ in range(3)]

        for item in nums:
            cache[item] += 1

        # for i in range(cache[0]):
        #     nums[i] = 0
        #
        # for i in range(cache[0], cache[0] + cache[1]):
        #     nums[i] = 1
        #
        # for i in range(cache[0] + cache[2], sum(cache)):
        #     nums[i] = 2

        for index in range(len(cache)):
            if index == 0:
                start = 0
            else:
                start = sum(cache[:index])

            for i in range(start, start + cache[index]):
                nums[i] = index

    def quick_sort_3_way(self, nums):
        zero = -1  # the initial nums not assume 0 is at index 0
        two = len(nums)  # 2 should not be assumed to at index n-1

        i = 0
        while i < two:
            # 00000011111112222222, 1 is in middle
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                two -= 1  # there is two, two decr 1 to the unknown number, swap
                nums[two], nums[i] = nums[i], nums[two]
            elif nums[i] == 0:
                zero += 1  # zero incr to the next unknown number, swap
                nums[zero], nums[i] = nums[i], nums[zero]
                i += 1
            else:
                raise ValueError("number not in scope 0,1,2 !")

    def quick_sort_3_way_1(self, nums):
        # if initialize point like below, i could equal to point two
        zero = 0
        two = len(nums) - 1

        i = 0
        while i <= two:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[two], nums[i] = nums[i], nums[two]
                two -= 1
            elif nums[i] == 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1
                i += 1
            else:
                raise ValueError


if __name__ == "__main__":
    test_input = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(test_input)
    print(test_input)

