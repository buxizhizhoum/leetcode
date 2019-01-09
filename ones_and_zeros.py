#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
In the computer world, use restricted resource you have to generate maximum
benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively.
On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with
given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:
The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.
Example 1:
Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: There are totally 4 strings can be formed by the using of 5 0s and 3 1s,
which are “10”,0001”,”1”,”0”
Example 2:
Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
"""
from collections import Counter


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.recursion(strs, m, n)

    def recursion(self, strs, m, n):
        counter = {}
        for string in strs:
            counter[string] = Counter(string)

        # brute force
        # return self._recursion(strs, m, n, 0, counter)

        # memorization
        # memo = [[[None for l in range(n+1)] for k in range(m+1)] for i in range(len(strs))]
        # return self._recursion_memo(strs, m, n, 0, counter, memo)

        # dynamic programming
        # return self.dp(strs, m, n, counter)
        return self.dp_optimize(strs, m, n, counter)

    def _recursion(self, strs, m, n, index, counter):
        if m <= 0 and n <= 0 or index >= len(strs):
            return 0

        # res = -1
        res = 0
        for i, string in enumerate(strs[index:], start=index):
            string_count = counter[string]

            m_cost = string_count.get("0", 0)  # how many zeros it will cost
            n_cost = string_count.get("1", 0)  # how many ones it will cost
            if m >= m_cost and n >= n_cost:
                # recursion from i+1
                tmp = self._recursion(strs, m-m_cost, n-n_cost, i+1, counter)
                # if tmp != -1:
                #     res = max(res, 1+tmp)
                res = max(res, 1 + tmp)
        return res

    def _recursion_memo(self, strs, m, n, index, counter, memo):
        # todo: TLE
        if m <= 0 and n <= 0 or index >= len(strs):
            return 0

        if memo[index][m][n] is not None:
            return memo[index][m][n]

        # res = -1
        res = 0
        for i, string in enumerate(strs[index:], start=index):
            string_count = counter[string]

            m_cost = string_count.get("0", 0)  # how many zeros it will cost
            n_cost = string_count.get("1", 0)  # how many ones it will cost
            if m >= m_cost and n >= n_cost:
                # recursion from i+1
                tmp = self._recursion_memo(strs, m-m_cost, n-n_cost, i+1, counter, memo)
                # if tmp != -1:
                #     res = max(res, 1+tmp)
                res = max(res, 1 + tmp)
        memo[index][m][n] = res
        return res

    def dp(self, strs, m, n, counter):
        if m <= 0 and n <= 0 or len(strs) == 0:
            return 0
        # a 3D list
        memo = [[[0 for l in range(n+1)] for k in range(m+1)] for i in range(len(strs))]
        # initialize memo, only for first string, how many string it could assemble
        # it is the top side of the 3D memo
        string_0_count = Counter(strs[0])
        for k in range(m+1):
            for l in range(n+1):
                if k >= string_0_count.get("0", 0) and l >= string_0_count.get("1", 0):
                    memo[0][k][l] = 1

        for i in range(1, len(strs)):
            string_count = counter[strs[i]]
            for k in range(m+1):
                for l in range(n+1):
                    # how many zeros it will cost
                    m_cost = string_count.get("0", 0)
                    # how many ones it will cost
                    n_cost = string_count.get("1", 0)
                    if k >= m_cost and l >= n_cost:
                        # memo[i-1][k][l] is value in mesh above current pos
                        # memo[i-1][k-m_cost][l-n_cost] is the value consider current element
                        memo[i][k][l] = max(memo[i-1][k][l], 1 + memo[i-1][k-m_cost][l-n_cost])
                    else:
                        memo[i][k][l] = memo[i-1][k][l]
        return memo[len(strs)-1][m][n]

    def dp_optimize(self, strs, m, n, counter):
        # optimize to reduce space complexity
        if m <= 0 and n <= 0 or len(strs) == 0:
            return 0
        # a 3D list
        # optimization: 2 layers are enough
        memo = [[[0 for l in range(n+1)] for k in range(m+1)] for i in range(2)]
        # initialize memo, only for first string, how many string it could assemble
        # it is the top side of the 3D memo
        string_0_count = Counter(strs[0])
        for k in range(m+1):
            for l in range(n+1):
                if k >= string_0_count.get("0", 0) and l >= string_0_count.get("1", 0):
                    memo[0][k][l] = 1

        for i in range(1, len(strs)):
            string_count = counter[strs[i]]
            cur = i % 2
            prev = (i-1) % 2
            for k in range(m+1):
                for l in range(n+1):
                    # how many zeros it will cost
                    m_cost = string_count.get("0", 0)
                    # how many ones it will cost
                    n_cost = string_count.get("1", 0)
                    if k >= m_cost and l >= n_cost:
                        # memo[i-1][k][l] is value in mesh above current pos
                        # memo[i-1][k-m_cost][l-n_cost] is the value consider current element
                        # memo[i%2][k][l] = max(memo[(i-1)%2][k][l], 1 + memo[(i-1)%2][k-m_cost][l-n_cost])
                        memo[cur][k][l] = max(memo[prev][k][l], 1 + memo[prev][k-m_cost][l-n_cost])
                    else:
                        memo[cur][k][l] = memo[prev][k][l]
        return memo[(len(strs)-1)%2][m][n]


if __name__ == "__main__":
    test_strs = ["10", "0001", "111001", "1", "0"]
    test_m = 5
    test_n = 3
    print(Solution().findMaxForm(test_strs, test_m, test_n))


