#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
import math


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # return self.basic(n)
        return self.grid_search(n)

    def basic(self, n):
        """
        time limit exceeded
        :param n:
        :return:
        """
        res = 0
        for i in range(n):
            if self.is_prime(i):
                res += 1
        return res

    def is_prime(self, n):
        """
        check whether n is a prime

        check whether n could be divided by a number in range(2, int(sqrt(n))+1)
        :param n:
        :return:
        """
        if n <= 1:
            return False
        elif 1 < n < 4:
            return True
        else:
            n_sqrt = int(math.sqrt(n))
            for i in range(2, n_sqrt + 1):
                # tmp = float(n) / i
                # if int(tmp) == tmp:
                if n % i == 0:
                    return False
        return True

    def grid_search(self, n):
        """
        Sieve of Eratosthenes
        :param n:
        :return:
        """
        if n <= 1:
            return 0
        # cache = {i: False for i in range(2, n)}
        # cache = [False for _ in range(2, n)]
        cache = [False for _ in range(n)]

        # for k in range(2, n):  # to sqrt n is enough
        for k in range(2, int(math.sqrt(n)) + 1):  # to sqrt n is enough
            v = cache[k]
            if v is False:
                # if current number is prime, multiply it from 2 to n // k + 1
                # mark number that could reach to not prime
                for i in range(2, n // k + 1):
                    # if a number could be get by multiple k,
                    # it means it is prime
                    if i*k < n:
                        # if index is legal, set it True
                        cache[i*k] = True
        # count it
        res = 0
        for v in cache[2:]:  # start from 2, 0 and 1 is just to fill head
            if v is False:
                res += 1

        return res


if __name__ == "__main__":
    # print(Solution().countPrimes(10))
    print(Solution().countPrimes(999983))

