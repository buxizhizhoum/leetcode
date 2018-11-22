#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        answer = []
        numbers = range(1, n+1)
        # self.find_combination(res, answer, numbers, k)
        self.find_combination_2(res, answer, numbers, k)
        return res

    def find_combination(self, res, answer, numbers, k):
        if k == 0:
            res.append(answer)
            return res

        for i in range(0, len(numbers)):
            current_num = numbers[i]

            self.find_combination(res, answer + [current_num], numbers[i+1:], k - 1)

    def find_combination_2(self, res, answer, numbers, k):
        if k == 0:
            # import copy
            # res.append(copy.copy(answer))
            res.append(answer[:])
            return res

        for i in range(0, len(numbers)):
            current_num = numbers[i]

            answer.append(current_num)
            self.find_combination_2(res, answer, numbers[i+1:], k - 1)
            answer.pop()


if __name__ == "__main__":
    print(Solution().combine(3, 2))




