#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res =[]
        answer = []
        self._find_combination(candidates, target, res, answer)
        return res

    def _find_combination(self, candicates, target, res, answer):
        if target == 0:
            # to ensure no duplicated combination in res
            # todo: is there any better method?
            sort_ans = sorted(answer)
            if sort_ans not in res:
                res.append(sort_ans)
            return

        if target < 0:
            return

        for i in range(len(candicates)):
            current_num = candicates[i]
            # self._find_combination(candicates[:i] + candicates[i+1:], target-current_num, res, answer + [current_num])
            # candicates[i+1:] means used element will not occur again.\
            # this is combination, draw a tree if necessary
            self._find_combination(candicates[i+1:], target-current_num, res, answer + [current_num])


if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(Solution().combinationSum2(candidates, target))









