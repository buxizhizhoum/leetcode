#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
"""


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True

        return self.ans(num)

    def ans(self, num):
        if num in (2,3,5):
            return True

        for i in (2,3,5):
            div, mod = divmod(num, i)
            if mod == 0:
                tmp = self.ans(div)
                if tmp is True:
                    return True
        return False

    def isprime(self, num):
        if num == 1:
            return False
        if num == 2:
            return True

        i = 2
        while i * i <= num:
            if i != 1 and num % i == 0:
                # there are other factors besides 1 and itself
                return False
            i += 1

        return True


if __name__ == "__main__":
    # for i in range(2, 10):
    #     print(Solution().isprime(i))

    for i in (1,2,8,14):
        print(Solution().isUgly(i))

