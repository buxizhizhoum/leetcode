#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

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
        return self.ans(prices)

    def ans(self, prices):
        """
        could be optimized to use O(1) space
        :param prices:
        :return:
        """
        will_incr = []
        for day, price in enumerate(prices[:-1]):
            if price < prices[day+1]:
                will_incr.append(True)
            else:
                will_incr.append(False)
        # the last day, no future, add False
        will_incr.append(False)

        profit = 0
        buy_price = None
        for day, price in enumerate(prices):
            if will_incr[day] is False and buy_price is not None:
                # if it is to decr, price today is peak, sell and get profit
                profit = profit + (price - buy_price)
                buy_price = None

            elif will_incr[day] is True:
                # if it is to incr, price today is vally
                if buy_price is None:
                    # if not buy yet, buy it
                    buy_price = price
                else:
                    # if buyed, check to ensure buy on vally
                    buy_price = min(buy_price, price)

        return profit


if __name__ == "__main__":
    # test_prices = [7, 1, 5, 3, 6, 4]
    # test_prices = [7,6,4,3,1]
    test_prices = [1, 2, 3, 4, 5]
    print(Solution().maxProfit(test_prices))

