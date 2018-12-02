#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Given an array of integers, return indices of the two numbers such that
they add up to a specific target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

links: https://leetcode.com/problems/two-sum/description/
"""


# class Solution(object):
#     """
#     answer from web
#     """
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         if len(nums) < 2:
#             return False
#         dic = {}
#         for index, num in enumerate(nums):
#             if num in dic:
#                 return [dic[num], index]
#             # buffer the index of the other value and index of current value
#             # {target - num : index of num}, if target - num = new num
#             else:
#                 dic[target - num] = index


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # return self.dict_buffer(nums, target)
        return self.dict_buffer_list(nums, target)

    def dict_buffer(self, nums, target):
        """
        the buffer is gradually increasing with for loop
        :param nums:
        :param target:
        :return:
        """
        if len(nums) < 2:
            return False

        index_buffer = {}
        for index, num in enumerate(nums):
            diff = target - num
            diff_index = index_buffer.get(diff)
            if diff_index is None:
                index_buffer[num] = index
            else:
                if diff_index != index:
                    return sorted([index, diff_index])
        return False

    def dict_buffer_list(self, nums, target):
        """
        attention, if there are duplicate element in the list, the indexes are
        sorted in a list whose key is the num
        
        eg: nums = [1,2,3,2]
        index_buffer = {1:[0], 2:[1,3], 3:[2]}
        :param nums:
        :param target:
        :return:
        """
        if len(nums) < 2:
            return

        index_buffer = {}
        for index, num in enumerate(nums):
            if index_buffer.get(num) is None:
                index_buffer[num] = [index]
            else:
                index_buffer[num].append(index)

        for index, num in enumerate(nums):
            diff = target - num
            if index_buffer.get(diff) is not None:
                index_l = index_buffer[diff]

                for i in index_l:
                    if i != index:
                        return sorted([index, i])
        return False

    def brute(self, nums, target):
        res = None
        if len(nums) < 2:
            return res

        for index, num in enumerate(nums):
            # the residual
            tmp = target - num
            # if residual in nums, search its index
            if tmp in nums:
                for i, item in enumerate(nums):
                    if item == tmp and i != index:
                        res = [index, i]
                        return res
        return res


if __name__ == "__main__":
    test_list = [2, 7, 11, 15]
    test_list = [2, 5, 5, 11]
    solution = Solution()
    print solution.twoSum(test_list, 10)
