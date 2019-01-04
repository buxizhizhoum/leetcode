#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers.
Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:

Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199.
             1 + 99 = 100, 99 + 100 = 199
"""


class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # return self.recursion(num)
        memo = {}
        return self.recursion_cache(num, memo)

    def recursion(self, string):
        length = len(string)
        if length == 0:
            return True

        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    # string[:i+1] is the first number
                    # string[i+1: j+1] is the second number
                    # string[j+1: k+1] is the third number
                    first = string[:i+1]
                    second = string[i+1:j+1]
                    third = string[j+1:k+1]

                    if int(first) != 0 and first.startswith("0"):
                        continue

                    if int(second) != 0 and second.startswith("0"):
                        continue

                    if int(third) != 0 and third.startswith("0"):
                        continue

                    if int(first) + int(second) == int(third):
                        # k < length means the tail of string is reached
                        if k == length - 1:
                            return True
                        elif k < length-1 and self.recursion(string[i+1:]) is True:
                            return True

        return False

    # def recursion_cache(self, string, memo):
    #     # basic cache version
    #     length = len(string)
    #     if length == 0:
    #         return True
    #
    #     if memo.get(string) is not None:
    #         return memo.get(string)
    #
    #     # for i in range(length):
    #     for i in range(length // 2 + 1):  # optimize
    #         for j in range(i + 1, length):
    #             for k in range(j + 1, length):
    #                 # string[:i+1] is the first number
    #                 # string[i+1: j+1] is the second number
    #                 # string[j+1: k+1] is the third number
    #                 first = string[:i + 1]
    #                 second = string[i + 1:j + 1]
    #                 third = string[j + 1:k + 1]
    #
    #                 if int(first) != 0 and first.startswith("0"):
    #                     continue
    #
    #                 if int(second) != 0 and second.startswith("0"):
    #                     continue
    #
    #                 if int(third) != 0 and third.startswith("0"):
    #                     continue
    #
    #                 if int(first) + int(second) == int(third):
    #                     # k < length means the tail of string is reached
    #                     if k == length - 1:
    #                         memo[string] = True
    #                         return True
    #                     elif k < length - 1 and self.recursion_cache(
    #                             string[i + 1:], memo) is True:
    #                         memo[string] = True
    #                         return True
    #     memo[string] = False
    #     return False

    def recursion_cache(self, string, memo):
        length = len(string)
        if length == 0:
            return True

        if memo.get(string) is not None:
            return memo.get(string)

        # for i in range(length):
        for i in range(length // 2 + 1):  # optimize
            # string[:i+1] is the first number
            first = string[:i + 1]
            for j in range(i+1, length):
                # string[i+1: j+1] is the second number
                second = string[i + 1:j + 1]
                if int(first) != 0 and first.startswith("0"):
                    continue
                if int(second) != 0 and second.startswith("0"):
                    # could stop advance
                    break

                third = str(int(first) + int(second))
                # starts with is an optimize
                if string[j+1:].startswith(third):
                    # if reaches the end of string, return
                    if j + 1 + len(third) == length:
                        return True
                    # if did not reach the end, continue recursion
                    elif j + 1 + len(third) < length and self.recursion_cache(string[i+1:], memo) is True:
                        return True

        memo[string] = False
        return False


if __name__ == "__main__":
    test_input = "112358"
    # test_input = "199100199"
    # test_input = "1023"
    print(Solution().isAdditiveNumber(test_input))






