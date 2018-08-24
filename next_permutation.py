#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        decr_index = self.find_decr_element(nums)
        next_index = self.find_next_element(nums, decr_index)
        # swap
        if decr_index is not None and next_index is not None:
            nums[decr_index], nums[next_index] = nums[next_index], nums[decr_index]

        if decr_index is not None:
            self.reverse(nums, decr_index + 1, len(nums) - 1)

        if decr_index is None:
            nums.sort()

    @staticmethod
    def find_decr_element(nums):
        for i in range((len(nums) - 1), 0, -1):
            if nums[i] > nums[i - 1]:
                return i - 1

    @staticmethod
    def find_next_element(nums, start):
        if start is None:
            return None

        base = nums[start]
        for i in range(len(nums) - 1, start - 1, -1):
            if nums[i] > base:
                return i

        if nums[len(nums) - 1] > nums[start]:
            return len(nums) - 1  # element is at the end of the list
        else:
            return None

    @staticmethod
    def reverse(nums, start, end):
        left, right = start, end
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums


if __name__ == "__main__":
    l = [1,5,8,4,7,6,5,3,1]
    l = [1,5,1]
    # l = [1,2,3]
    # l = [1]
    # l = [1,3,2]
    # l = [1,2,3]
    solution = Solution()
    solution.nextPermutation(l)
    print(l)



