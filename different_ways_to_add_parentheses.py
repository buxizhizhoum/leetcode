#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
"""


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        # return self.recursion(input)
        memo = {}
        return self.recursion_cache(input, memo)

    def recursion(self, input):
        # divide and conquer
        length = len(input)
        if length == 0:
            return

        if input.isdigit():
            return [int(input)]

        res = []
        for i, char in enumerate(input):
            if char in ("+", "-", "*"):
                res_l = self.recursion(input[:i])
                res_r = self.recursion(input[i+1:])

                for tmp_l in res_l:
                    for tmp_r in res_r:
                        res.append(self.helper(tmp_l, tmp_r, char))
        return res

    def recursion_cache(self, input, memo):
        # divide and conquer
        length = len(input)
        if length == 0:
            return

        if input.isdigit():
            return [int(input)]

        if memo.get(input) is not None:
            return memo.get(input)

        res = []
        for i, char in enumerate(input):
            if char in ("+", "-", "*"):
                res_l = self.recursion_cache(input[:i], memo)
                res_r = self.recursion_cache(input[i+1:], memo)

                for tmp_l in res_l:
                    for tmp_r in res_r:
                        res.append(self.helper(tmp_l, tmp_r, char))
        memo[input] = res
        return res

    def helper(self, num_l, num_r, op):
        if op == "+":
            return int(num_l) + int(num_r)
        elif op == "-":
            return int(num_l) - int(num_r)
        elif op == "*":
            return int(num_l) * int(num_r)


if __name__ == "__main__":
    test_str = "2*3-4*5"
    print(Solution().diffWaysToCompute(test_str))

    # todo: try dp

