#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n^2) complexity.
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.basic(nums)

    def basic(self, nums):
        if len(nums) == 1:
            return 1

        memo = [[-1 for _ in range(len(nums) + 1)] for _ in range(len(nums))]

        res = 0
        # for i in range(len(nums)):
            # res = max(res, self._recursion(nums, i, float("-inf")))
            # res = max(res, self._recursion_memorize(nums, i, -1, memo))

        # return res
        res = max(res, self._recursion(nums, 0, float("-inf")))
        # todo: -1 is Sentinel?
        # res = max(res, self._recursion_memorize(nums, 0, -1, memo))
        return res

    # def _recursion(self, nums, index, base):
    #     if index > len(nums)-1:
    #         return 0
    #
    #     # calculate max increasing sub sequence on nums[index+1:]
    #     res = 1
    #     for i in range(index + 1, len(nums)):
    #         if nums[i] > base:
    #             # count nums[i], res should + 1
    #             res = max(res, 1 + self._recursion(nums, i, nums[i]))
    #         else:  # nums[i] <= cur
    #             # do not count nums[i], res should not add 1
    #             res = max(res, self._recursion(nums, i, base))
    #
    #     return res

    def _recursion(self, nums, index, base):
        if index > len(nums)-1:
            return 0

        # calculate max increasing sub sequence on nums[index+1:]
        res_1 = 0
        if nums[index] > base:
            # count nums[i], res should + 1
            # todo: try recursion from tail to head, no matter how, it is from large string to small string
            res_1 = 1 + self._recursion(nums, index + 1, nums[index])
        # nums[i] <= cur
        # do not count nums[i], res should not add 1
        res_2 = self._recursion(nums, index+1, base)

        return max(res_1, res_2)

    # def _recursion_memorize(self, nums, index, base, memo):
    #     if index > len(nums)-1:
    #         return 0
    #
    #     if memo[index] != -1:
    #         return memo[index]
    #
    #     # calculate max increasing sub sequence on nums[index+1:]
    #     res = 1
    #     for i in range(index + 1, len(nums)):
    # todo: at every step, taken and not taken should be evaluated, and get max of them
    #         if nums[i] > base:
    #             res = max(res, 1 + self._recursion_memorize(nums, i, nums[i], memo))
    #         else:  # nums[i] <= cur
    #             res = max(res, self._recursion_memorize(nums, i, base, memo))
    #
    #     memo[index] = res
    #     return res

    def _recursion_memorize(self, nums, index, base_index, memo):
        # todo: attention, three are 2 changing parameters, memo is 2D
        if index > len(nums)-1:
            return 0

        if memo[index][base_index+1] != -1:
            return memo[index][base_index+1]

        # calculate max increasing sub sequence on nums[index+1:]
        res_1 = 0
        if base_index < 0 or nums[index] > nums[base_index+1]:
            # count nums[i], res should + 1
            res_1 = 1 + self._recursion_memorize(nums, index + 1, index, memo)
        # nums[i] <= cur
        # do not count nums[i], res should not add 1
        res_2 = self._recursion_memorize(nums, index+1, base_index, memo)

        memo[index][base_index+1] = max(res_1, res_2)
        return memo[index][base_index+1]

    def _recursion_1(self, nums, index, base):
        if index > len(nums)-1:
            return 0

        # calculate max increasing sub sequence on nums[index+1:]
        taken = 0
        if nums[index] > base:
            # count nums[i], res should + 1
            taken = 1 + self._recursion_1(nums, index + 1, nums[index])
        # do not count nums[i], res should not add 1
        not_taken = self._recursion_1(nums, index+1, base)

        return max(taken, not_taken)

    def _recursion_1_memorize(self, nums, index, base, memo):
        if index > len(nums)-1:
            return 0

        if memo[index] != -1:
            return memo[index]
        # calculate max increasing sub sequence on nums[index+1:]
        taken = 0
        if nums[index] > base:
            # count nums[i], res should + 1
            taken = 1 + self._recursion_1_memorize(nums, index + 1, nums[index], memo)
        # do not count nums[i], res should not add 1
        not_taken = self._recursion_1_memorize(nums, index+1, base, memo)

        memo[index] = max(taken, not_taken)
        return max(taken, not_taken)

    def dp(self, nums):
        length = len(nums)
        if length == 0:
            return 0

        # since every element have at least one increasing sub sequence,
        # it should be initialized to a all 1 array
        memo = [1 for _ in nums]
        # memo[length - 1] = 1  # this is not enough
        # memo = [1 for _ in nums]  # merge initialize together
        # from end to beginning, if nums[i] < nums[j], means there is possibility
        # to produce a sub sequence that is longer, memo[j] + 1 is possible to
        # be larger than memo[i]
        for i in range(length-2, -1, -1):
            for j in range(length - 1, i, -1):
                if nums[j] > nums[i]:
                    # if nums[j] > nums[i],
                    # the sub sequence consist of nums[j] and memo[j] might be larger than memo[i]
                    memo[i] = max(memo[i], memo[j] + 1)

        res = max(memo)
        return res

    def dp_1(self, nums):
        length = len(nums)
        if length == 0:
            return 0

        memo = [1 for _ in nums]
        # from beginning to end
        for i in range(1, length):
            # check how many element in [0, i) is less than nums[i]
            for j in range(0, i):
                if nums[j] < nums[i]:
                    memo[i] = max(memo[i], memo[j] + 1)

        return max(memo)


if __name__ == "__main__":
    test_nums = [10, 9, 2, 5, 3, 7, 101, 18]
    test_nums = [-2, -1]
    test_nums = [2, 2]
    test_nums = [10, 9, 2, 5, 3, 4]
    # test_nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    print(Solution().basic(test_nums))
    # print(Solution()._recursion_1(test_nums, 0, test_nums[0]))
    print(Solution().dp(test_nums))
    print(Solution().dp_1(test_nums))


