#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e.,
buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # return self.ans(prices)
        # return self.ans_1(prices)
        return self.ans_2(prices)

    def ans(self, prices):
        """
        brute force
        :param prices:
        :return:
        """
        profit = 0
        for buy_day, buy_price in enumerate(prices[:len(prices)-1]):
            for sell_day, sell_price in enumerate(prices[buy_day:], start=buy_day):
                profit = max(profit, sell_price - buy_price)

        return profit

    def ans_1(self, prices):
        """
        3 pass
            1st to find the minimum price to buy so far
            2nd find the maximum price to sell in future
            3rd find the day to buy and sell
        :param prices:
        :return:
        """
        if not prices:
            return 0

        # minimum prices so far
        min_prices = [prices[0]]
        for buy_day, price in enumerate(prices[1:], start=1):
            tmp = min(min_prices[buy_day-1], price)
            min_prices.append(tmp)

        # maximum prices in the future
        max_prices = [prices[-1]]
        for sell_day in range(len(prices)-2, -1, -1):
            tmp = max(max_prices[-1], prices[sell_day])
            max_prices.append(tmp)
        max_prices.reverse()

        profit = 0
        for day in range(len(prices)-1):
            buy_price = min_prices[day]
            sell_price = max_prices[day+1]
            profit = max(profit, sell_price - buy_price)
        return profit

    def ans_2(self, prices):
        """
        one pass
        :param prices:
        :return:
        """
        if not prices:
            return 0

        profit = 0
        min_price = prices[0]

        for price in prices[1:]:
            # calculate profit based on min_price so far
            profit = max(profit, price - min_price)
            # update min price
            min_price = min(price, min_price)
        return profit


if __name__ == "__main__":
    test_prices = [7, 1, 5, 3, 6, 4]
    # test_prices = [7,6,4,3,1]
    print(Solution().maxProfit(test_prices))
    # print(Solution().ans_2(test_prices))



