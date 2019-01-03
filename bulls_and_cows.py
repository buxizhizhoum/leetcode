#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows.

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
"""
from collections import Counter


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        return self.ans(secret, guess)

    def ans(self, secret, guess):
        secret_dict = self.str2dict(secret)
        guess_dict = self.str2dict(guess)

        bulls = 0
        cows = 0
        for k, secret_locations in secret_dict.iteritems():
            if k in guess_dict:
                guess_locations = guess_dict[k]
                # todo: Attention, counter is enough
                # min(count_s[char] - count_g[char]]) - tmp_bulls
                # tmp_bulls could be get with for i, j in zip(s, g).
                tmp_bulls = len(secret_locations.intersection(guess_locations))
                tmp_cows = min(len(secret_locations), len(guess_locations)) - tmp_bulls
                bulls += tmp_bulls
                cows += tmp_cows

        return "%sA%sB" % (bulls, cows)

    def str2dict(self, string):
        cache = {}
        for index, char in enumerate(string):
            if char in cache:
                cache[char].add(index)
            else:
                cache[char] = set([index])

        return cache

    def ans_1(self, secret, guess):
        count_s = Counter(secret)
        count_g = Counter(guess)

        bulls = 0
        for i, j in zip(secret, guess):
            if i == j:
                bulls += 1

        cows = 0
        for k, v in count_s.iteritems():
            if k in count_g:
                cows += min(count_s[k], count_g[k])

        cows -= bulls

        return "%sA%sB" % (bulls, cows)


if __name__ == "__main__":
    secret = "1807"
    guess = "7810"
    # secret = "1123"
    # guess = "0111"
    print(Solution().getHint(secret, guess))
    print(Solution().ans_1(secret, guess))

