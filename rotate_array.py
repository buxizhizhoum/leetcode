#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # self.cyclic_replacement(nums, k)
        self.slice(nums, k)

    def slice(self, nums, k):
        if k == 0:
            return nums

        if len(nums) <= 1:
            return nums

        if k == len(nums):
            return nums

        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:len(nums)-k]

    def cyclic_replacement(self, nums, k):
        """
        test could not pass
        :param nums:
        :param k:
        :return:
        """
        length = len(nums)
        if length <= 1:
            return nums

        if k == length:
            return nums

        k = k % length  # if k is larger than length, save unnecessary rotate
        tmp = nums[0]
        for i in range(k):
            for j in range(length//k+1):
                # get the element where nums[i] to locate and cache it
                if i + (j+1)*k < length:
                    # the index of element to be replaced
                    destination = i + (j+1)*k
                else:
                    destination = i + (j+1)*k - length

                # cache the element to be replaced
                cache = nums[destination]
                # replace
                nums[destination] = tmp
                tmp = cache


if __name__ == "__main__":
    test_num = [1, 2, 3, 4, 5, 6, 7]
    # test_num = [1, 2]
    test_k = 2
    # test_num = [-1,-100,3,99]
    # test_k = 3
    Solution().rotate(test_num, test_k)
    print(test_num)



