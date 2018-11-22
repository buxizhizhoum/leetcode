#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # numbers = range(1, n + 1)
        numbers = range(1, 10)
        res = []
        answer = []
        target = n
        self.find_combination(res, answer, numbers, k, target)
        return res

    def find_combination(self, res, answer, numbers, k, target):
        if k == 0:
            if target == 0:
                res.append(answer)
            return
        if k < 0:
            return

        for i in range(len(numbers)):
            current_num = numbers[i]
            # optimize, but seems no use
            # if current_num > target:
            #     return
            self.find_combination(res, answer + [current_num], numbers[i+1:], k-1, target-current_num)


if __name__ == "__main__":
    k = 3
    n = 7
    print(Solution().combinationSum3(k, n))




