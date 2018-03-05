#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a sorted array, remove the duplicates in-place such that each element
appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # when deleting item in a list, start from end,
        # otherwise there will be index out of range Error
        for index in range(len(nums) - 1, 0, -1):
            if nums[index] == nums[index - 1]:  # judge with == not in.
                del nums[index]

        return len(nums)

        # duplicate = 0
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         duplicate += 1
        #     nums[i - duplicate] = nums[i]
        #
        # return len(nums) - duplicate


if __name__ == "__main__":
    test_list = [1, 1, 2, 2, 3, 3]
    # test_list = [1, 1, 1, 1]
    # test_list = range(100000)
    # test_list = []
    solution = Solution()
    print solution.removeDuplicates(test_list)