#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

Example:

Input: 4
Output: false
Explanation: If there are 4 stones in the heap, then you will never win the game;
             No matter 1, 2, or 3 stones you remove, the last stone will always be
             removed by your friend.
"""
import sys
sys.setrecursionlimit(1500)


class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # return self.recursion_basic(n) % 2 == 0
        # return self.recursion(n) % 2 == 1
        memo = {}
        return self.recursion_memorize(n, memo) % 2 == 1

    def recursion_basic(self, n):
        if n < 4:
            return 0

        for i in (1, 2, 3):
            tmp = 1 + self.recursion(n-i)
            if tmp % 2 == 0:
                return 0

        return 1

    def recursion(self, n):
        # time limit exceeded
        if n < 4:
            # could be fetch in one time, return 1
            return 1

        for i in (1, 2, 3):
            tmp = 1 + self.recursion(n-i)
            # if could be fetch in o
            # if fetch 2 time, it could be regarded a new start
            if tmp % 2 == 1:
                return 1

        return 0

    def recursion_memorize(self, n, memo):
        # the maximum recursion depth exceeded
        if n < 4:
            return 1

        if memo.get(n) is not None:
            return memo.get(n)

        for i in (1, 2, 3):
            tmp = 1 + self.recursion_memorize(n-i, memo)
            if tmp % 2 == 1:
                memo[n] = 1
                return 1
        memo[n] = 0
        return 0

    # def iteration(self, n):
    #     fetch_time = 0
    #
    #     # while n > 3:
    #     #     fetch_time += 1
    #
    #         for i in (1,2,3):
    #
    #             n = n-i
    #             if n < 4:
    #                 break

    # def dp(self, n):
        # wrong answer
    #     if n <= 0:
    #         return False
    #     if n < 4:
    #         return True
    #
    #     memo = [False for _ in range(n+1)]
    #     for i in (1,2,3):
    #         memo[i] = False
    #
    #     for i in range(4, n+1):
    #         if memo[i-1] and memo[i-2] and memo[i-3]:
    #             memo[i] = False
    #
    #     return memo[n]


if __name__ == "__main__":
    print(Solution().canWinNim(5))
    # print(Solution().dp(5))

