#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # cache wordDict as set to optimize check
        word_set = set(wordDict)
        cache = {}
        return self.ans(s, word_set, cache)

    def ans_basic(self, s, word_set):
        """
        brute force
        :param s:
        :param word_set:
        :return:
        """
        if not s:
            return True

        for i in range(len(s)):
            word = s[:i + 1]
            if word in word_set:
                tmp = self.ans_basic(s[i + 1:], word_set)
                # if true, stop recursion advance
                if tmp is True:
                    return True
        return False

    def ans(self, s, word_set, cache):
        """
        recursion, dfs, optimize with memorization
        :param s:
        :param word_set:
        :param cache:
        :return:
        """
        if not s:
            return True

        # if it is already processed, return it res directly
        # if it could not break, stop advance
        # todo: Attention, this is to cache False case
        if cache.get(s) is not None:
            return cache.get(s)

        for i in range(len(s)):
            word = s[:i + 1]
            if word in word_set:
                tmp = self.ans(s[i + 1:], word_set, cache)
                # if true, stop recursion advance
                if tmp is True:
                    # cache res
                    # todo: Attention line below, it is not necessary
                    # it also works if line below is removed
                    # cache[s[i+1:]] = True
                    return True
        # means s cloud not break
        cache[s] = False
        return False


if __name__ == "__main__":
    test_s = "leetcode"
    test_wordDict = ["leet", "code"]

    test_s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    test_wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa",
                     "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]

    # test_s = "catsandog"
    # test_wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(Solution().wordBreak(test_s, test_wordDict))

    # todo: dp mesh
