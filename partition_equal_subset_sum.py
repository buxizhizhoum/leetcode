#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""


# similar to 0-1 package, convert to fill a package whose capacity is sum/2
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_all = sum(nums)
        if sum_all % 2 != 0:  # no way to partition sum to two part
            return False

        # return self.recursion(nums, sum_all)
        return self.dp(nums)

    def recursion(self, nums, sum_all):
        # return self._recursion(nums, len(nums)-1, sum_all//2)

        # len(nums) is the count of rows and sum_all // 2 + 1 is the col count
        memo = [[None for j in range(sum_all//2+1)] for _ in range(len(nums))]
        return self._recursion_memo(nums, len(nums)-1, sum_all//2, memo)

    def _recursion(self, nums, index, sum_total):
        if sum_total == 0:
            return True

        if index < 0 or sum_total < 0:
            # could not fill the package
            return False

        return self._recursion(nums, index-1, sum_total) or \
                    self._recursion(nums, index-1, sum_total - nums[index])

    def _recursion_memo(self, nums, index, sum_total, memo):
        # the diff parameters is index and sum_total, so a 2D list is needed
        # to cache the duplicated res
        if sum_total == 0:
            return True

        if index < 0 or sum_total < 0:
            # could not fill the package
            return False

        if memo[index][sum_total] is not None:
            return memo[index][sum_total]

        memo[index][sum_total] = self._recursion_memo(nums, index-1, sum_total, memo) \
                                 or self._recursion_memo(nums, index-1, sum_total - nums[index], memo)

        return memo[index][sum_total]

    def dp(self, nums):
        sum_all = sum(nums)
        length = len(nums)

        memo = [[None for j in range(sum_all//2+1)] for _ in range(length)]
        # initialize memo
        for i in range(sum_all//2+1):
            # whether first number could fill first package,
            # since it is exactly fill, it should be equal,
            # this is slightly different with 0-1 package
            memo[0][i] = (nums[0] == i)

        for i in range(1, length):
            for j in range(sum_all//2+1):
                memo[i][j] = memo[i-1][j] or memo[i-1][j-nums[i]]

        return memo[length-1][sum_all//2]


if __name__ == "__main__":
    test_nums = [1, 5, 11, 5]
    # test_nums = [1, 2, 3, 5]
    test_nums = [1, 1]
    print(Solution().canPartition(test_nums))




