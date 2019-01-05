#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        return self.basic(coins, amount)
        # return self.dp(coins, amount)

    def basic(self, coins, amount):
        # return self._recursion(coins, amount, 0)
        memo = [[None for j in range(amount+1)] for _ in range(len(coins))]
        return self._recursion_memo(coins, amount, 0, memo)

    def _recursion(self, coins, amount, index):
        """
        总共有多少amount,每一个地方的硬币放多少个，所以需要amount, 和index两个参数
        :param coins:
        :param amount:
        :param index:
        :return:
        """
        if amount == 0:
            return 0

        if index < len(coins) and amount > 0:
            # how many coin specified by index could hold at most
            max_amount = amount // coins[index]
            # try to put 0 to max_amount coin[index]
            res = float("inf")
            # todo: attention
            # 这里的关注点在于对于amount这个数字有多少中组合，取其中最小的，
            # 所以，递归的时候对每一枚硬币都尝试放0到最大可放的可能性
            # 然后取其中的最小值
            # 背包问题是尝试对于这一个商品放还是不放，所以对于每一个商品有两种可能
            # 这个为对于每一个硬币都有0到amount/币值种可能
            # 所以背包问题没有用到循环，每一次涉及到放与不放两种递归调用
            # 这个问题涉及了循环，需要遍历一个硬币的每种可能的个数
            for x in range(max_amount + 1):  # 遍历一个硬币的所有可能
                if amount < x*coins[index]:
                    # ensure add x coins not exceed total amount
                    continue
                # try put x coins[index], and then next coin
                tmp = self._recursion(coins, amount - x * coins[index], index+1)
                if tmp != -1:
                    res = min(res, tmp + x)  # 放了x个硬币的情况

            res = -1 if res == float("inf") else res
            return res
        else:
            return -1

    def _recursion_memo(self, coins, amount, index, memo):
        if amount == 0:
            return 0

        if index >= len(coins):
            return -1

        if memo[index][amount] is not None:
            return memo[index][amount]

        # how many coin specified by index could hold at most
        max_amount = amount // coins[index]
        # try to put 0 to max_amount coin[index]
        res = float("inf")
        # todo: attention
        # 这里的关注点在于对于amount这个数字有多少中组合，取其中最小的，
        # 所以，递归的时候对每一枚硬币都尝试放0到最大可放的可能性
        # 然后取其中的最小值
        # 背包问题是尝试对于这一个商品放还是不放，所以对于每一个商品有两种可能
        # 这个为对于每一个硬币都有0到amount/币值种可能
        # 所以背包问题没有用到循环，每一次涉及到放与不放两种递归调用
        # 这个问题涉及了循环，需要遍历一个硬币的每种可能的个数
        for x in range(max_amount + 1):  # 遍历一个硬币的所有可能
            if amount < x * coins[index]:
                # ensure add x coins not exceed total amount
                continue
            # try next coin
            tmp = self._recursion_memo(coins, amount - x * coins[index], index+1, memo)
            if tmp != -1:
                res = min(res, tmp + x)  # 放了x个硬币的情况

        res = -1 if res == float("inf") else res
        memo[index][amount] = res
        return res

    def dp(self, coins, amount):
        # time limit exceeded
        min_coin = min(coins)

        if amount == 0:
            return 0

        if amount < min_coin:
            # even could not hold the minimum coin
            return -1
        # capacity + 1, is to consider package [0, capacity]
        memo = [[-1 for j in range(amount+1)] for _ in range(len(coins))]

        # initialize
        for j in range(0, amount+1):
            # todo: attention sort coins is unnecessary
            if j % coins[0] == 0:
                memo[0][j] = j // coins[0]
            else:
                memo[0][j] = -1  # coins[0]凑不出amount j

        for i in range(1, len(coins)):
            for j in range(amount+1):
                # how many coin amount j could hold at most
                max_amount = j // coins[i]
                res = float("inf")
                # 不同于背包问题，这个for循环是由于这个问题的逻辑引入的，由于需要
                # 尝试在总量为j的情况，用值为coins[i]的硬币凑数，由于硬币可以
                # 无限使用，所以需要对于coins[i]的所有放入可能进行计算
                for x in range(max_amount + 1):
                    # todo: from large to smaller may be more faster
                    # if j >= x * coins[i] and memo[i - 1][j - x * coins[i]] != -1:
                    # j // coins[i] = max_amount >= x  ==>  j >= x*coins[i]
                    if memo[i - 1][j - x * coins[i]] != -1:
                        res = min(res, x + memo[i - 1][j - x * coins[i]])
                        memo[i][j] = res

        return memo[len(coins)-1][amount]


if __name__ == "__main__":
    import time
    test_coins = [1, 2, 5]
    test_amount = 11
    # test_coins = [2]
    # test_amount = 3
    # test_amount = 1
    #
    # # test_coins = [1]
    # # test_amount = 0
    #
    test_coins = [2]
    test_amount = 4

    test_coins = [2, 5, 10, 1]
    test_coins = [1, 2, 5, 10]
    test_amount = 27
    test_coins = [470, 35, 120, 81, 121]
    test_amount = 9825
    test_coins = [186,419,83,408]
    test_amount = 6249

    t1 = time.time()
    print(Solution().coinChange(test_coins, test_amount))
    print(time.time() - t1)


