#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


# class Solution(object):
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res = [nums, ]
#         for i in range(len(nums) - 1):
#             for item in res[:]:
#                 for j in range(i + 1, len(nums)):
#                     tmp = self.swap(i, j, item)
#                     res.append(tmp)
#         return res
#
#     @staticmethod
#     def swap(i, j, nums):
#         res = list(nums)
#         res[i], res[j] = res[j], res[i]
#         return res


# class Solution:
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         if len(nums) == 1:
#             return [nums]
#         else:
#             to_return = []
#             for i, x in enumerate(nums):
#                 for sub_result in self.permute(nums[:i]+ nums[i+1:]):
#                 # for sub_result in self.permute(nums):
#                     to_return.append([x] + sub_result)
#             return to_return


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return nums
        elif len(nums) == 2:
            tmp = list(nums)
            tmp[0], tmp[1] = tmp[1], tmp[0]
            return [nums, tmp]
        else:
            res = []
            i = 0
            length = len(nums)
            # this loop is only used to control loop times, let each element in
            # the list has a chance to be placed at the head of the result
            while i < length:

            # for i, ele in enumerate(nums):
            #     sub_res = self.permute(nums[1:])

                end_part = self.permute(nums[1:])
                for item in end_part:
                    res_tmp = nums[:1] + item
                    res.append(res_tmp)
                # swap element, make each element has the chance to be the head
                nums[0], nums[length - i - 1] = nums[length - i - 1], nums[0]
                i += 1
            return res


if __name__ == "__main__":
    l = range(1, 5)
    s = Solution()
    print(s.permute(l))


