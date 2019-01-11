#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
A sequence of numbers is called a wiggle sequence if the differences between
successive numbers strictly alternate between positive and negative.
The first difference (if one exists) may be either positive or negative.
A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3)
are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5]
are not wiggle sequences, the first because its first two differences are positive
and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence
that is a wiggle sequence. A subsequence is obtained by deleting some number of
elements (eventually, also zero) from the original sequence,
leaving the remaining elements in their original order.

Example 1:

Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.
Example 2:

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
Example 3:

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
"""


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.recursion(nums)

    def recursion(self, nums):
        if len(nums) < 2:
            return len(nums)
        # return 1 + max(self._recursion(nums, 0, True), self._recursion(nums, 0, False))
        memo = [[None for _ in (True, False)] for i in range(len(nums))]
        return 1 + max(self._recursion_memo(nums, 0, True, memo), self._recursion_memo(nums, 0, False, memo))

    def _recursion(self, nums, index, sign):
        """
        sign is the expectation of increasing or decreasing
        if sign is True, next element should be larger than current element
        else, next element should be smaller than current element
        :param nums:
        :param index:
        :param sign:
        :return:
        """
        # if len(nums[index:]) < 2:
        #     return len(nums[index:])

        res = 0
        for i in range(index+1, len(nums)):
            # sign is True, next element should be larger than current element
            if sign and nums[i] > nums[index]:
                # next expectation is decrease
                res = max(res, 1 + self._recursion(nums, i, not sign))
            # next element should be smaller than current element
            elif not sign and nums[i] < nums[index]:
                # expect next element is increasing
                res = max(res, 1 + self._recursion(nums, i, not sign))

        return res

    def _recursion_memo(self, nums, index, sign, memo):
        """
        sign is the expectation of increasing or decreasing
        if sign is True, next element should be larger than current element
        else, next element should be smaller than current element
        :param nums:
        :param index:
        :param sign: expectation of whether nums[i] is larger or less than next element
        :return:
        """
        if memo[index][sign] is not None:
            return memo[index][sign]

        res = 0
        for i in range(index+1, len(nums)):
            # sign is True, next element should be larger than current element
            if sign and nums[i] > nums[index]:
                # next expectation is decrease
                res = max(res, 1 + self._recursion_memo(nums, i, not sign, memo))
            # next element should be smaller than current element
            elif not sign and nums[i] < nums[index]:
                # expect next element is increasing
                res = max(res, 1 + self._recursion_memo(nums, i, not sign, memo))

        memo[index][sign] = res
        return res


if __name__ == "__main__":
    test_nums = [1, 7, 4, 9, 2, 5]
    test_nums = [33,53,12,64,50,41,45,21,97,35,47,92,39,0,93,55,40,46,69,42,6,95,51,68,72,9,32,84,34,64,6,2,26,98,3,43,30,60,3,68,82,9,97,19,27,98,99,4,30,96,37,9,78,43,64,4,65,30,84,90,87,64,18,50,60,1,40,32,48,50,76,100,57,29,63,53,46,57,93,98,42,80,82,9,41,55,69,84,82,79,30,79,18,97,67,23,52,38,74,15]
    print(Solution().wiggleMaxLength(test_nums))










