#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
"""
import math


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return self.ans(num)

    def ans(self, num):
        if num <= 1:
            return False
        divisors = []
        limit = int(math.floor(math.sqrt(num)))
        for i in range(1, limit + 1):
            if num % i == 0:
                divisors.append(i)

                if i != 1:
                    divisors.append(num / i)

        return sum(divisors) == num


if __name__ == "__main__":
    print(Solution().checkPerfectNumber(28))

