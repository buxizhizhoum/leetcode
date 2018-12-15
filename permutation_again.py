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


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        answer = []
        length = len(nums)
        # self.find_permute(nums, res, answer, length)
        res = self.backtracking(nums)
        return res

    def find_permute(self, nums, res, answer, length):
        # if len(nums) == 0 is enough.
        if len(nums) == 0 and len(answer) == length:
            res.append(answer)
            return

        for i in range(0,  len(nums)):
            current_num = nums[i]
            # nums[:i] + nums[i+1:] is the smaller list after num[i] is removed
            self.find_permute(nums[:i] + nums[i+1:], res, [current_num] + answer, length)

    # def backtracking(self, nums):
    #     # cache = [[] for _ in range(len(nums))]
    #     cache = []
    #     for i in range(len(nums)):
    #         cache.append([])
    #         for j in range(len(nums)):
    #             cache[i].append([])
    #     # initialize base condition
    #     for i in range(len(nums)):
    #         for j in range(len(nums)):
    #             if i == 0:
    #                 cache[i][j] = [[nums[i]]]
    #             if j == 0 and i != 0:
    #                 for digit in nums[:i+1]:
    #                     cache[i][j].append([digit])
    #
    #     for i in range(1, len(nums)):
    #         for j in range(1, len(nums)):
    #
    #             for ans in cache[i-1][j-1]:
    #                 insert nums[i] from start to end in every ans in cache[i-1][j-1]
    #                 for index in range(len(ans) + 1):
    #                     tmp = ans[::]
    #                     tmp.insert(index, nums[i])
    #                     cache[i][j].append(tmp)
    #
    #     return cache[len(nums)-1][len(nums)-1]

    def backtracking(self, nums):
        cache = []
        # initialize base condition, buffer result in a 2D list
        for i in range(len(nums)):
            cache.append([])
            for j in range(len(nums)):
                cache[i].append([])
                if i == 0:
                    cache[i][j].append([nums[i]])
                if j == 0 and i != 0:
                    for digit in nums[:i+1]:
                        cache[i][j].append([digit])

        for i in range(1, len(nums)):
            for j in range(1, len(nums)):
                # todo: Attention this is the core logic to solve this problem
                for ans in cache[i-1][j-1]:
                    # insert nums[i] from start to end in every ans in cache[i-1][j-1]
                    # considering insert is more expensive, use concat instead
                    for index in range(len(ans) + 1):
                        new_ans = ans[index:] + [nums[i]] + ans[:index]
                        cache[i][j].append(new_ans)

        return cache[len(nums)-1][len(nums)-1]


if __name__ == "__main__":
    test_nums = [1, 2, 3]
    print(Solution().permute(test_nums))





