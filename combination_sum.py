#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        answer = []
        # self._find_combination(res, answer, candidates, target)
        self._find_combination_2(res, answer, candidates, target)
        return res

    def _find_combination(self, res, answer, candidates, target):
        if target == 0:
            sort_ans = sorted(answer)
            if sort_ans not in res:
                res.append(sort_ans)
            return
        if target < min(candidates):
            return

        for item in candidates:
            # todo: Attention candidates is not chaged
            self._find_combination(res, answer + [item], candidates, target-item)

    def _find_combination_2(self, res, answer, candidates, target):
        """
        optimized version, candidates decrease along with recursion
        :param res:
        :param answer:
        :param candidates:
        :param target:
        :return:
        """
        if target == 0:
            sort_ans = sorted(answer)
            if sort_ans not in res:
                res.append(sort_ans)
            return
        if target < 0:
            return

        for i in range(len(candidates)):
            current_num = candidates[i]
            # todo: why not candidates[i+1:]? i is 0, will be always [0:] ... no use
            self._find_combination_2(res, answer + [current_num], candidates[i:], target-current_num)


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum(candidates, target))








