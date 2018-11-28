#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers:
            return
        # if target == 0:
        #     return

        for i in range(len(numbers)):
            diff = target - numbers[i]
            diff_index = self.binary_search(numbers, diff, i, len(numbers)-1)
            if diff_index is not None and diff_index != i:
                return sorted([i+1, diff_index+1])

    # def binary_search(self, numbers, target, start, end):
    #     mid = start + (end - start)//2
    #     if target == numbers[mid]:
    #         return mid
    #
    #     if start == end:
    #         return
    #
    #     if target > numbers[mid]:
    #         start = mid + 1
    #     else:
    #         end = mid - 1
    #     self.binary_search(numbers, target, start, end)

    def binary_search(self, numbers, target, start, end):
        while start <= end:
            mid = start + (end - start) // 2

            if target == numbers[mid]:
                return mid

            elif target > numbers[mid]:
                start = mid + 1
            else:
                end = mid - 1


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9

    numbers = [0, 0,3,4]
    target = 0
    numbers = [1,2,3,4,4,9,56,90]
    target = 8
    print(Solution().twoSum(numbers, target))


