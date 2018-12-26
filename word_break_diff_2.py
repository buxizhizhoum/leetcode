#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        word_set = set(wordDict)
        cache = {}
        res = []
        answer = []
        return self.format_res(self.recursion(s, word_set, cache))
        # return self.recursion_basic_1(s, word_set)
        # return res

    def recursion(self, s, word_set, cache):
        """
        backtracking optimized with memorization
        :param s: string to check
        :param word_set:
        :param cache: a dict used to memorize
        :return:
        """
        if not s:
            return [[], ]  # end
        # if s in word_set:  # another stop condition
        #     return [[s], ]

        if cache.get(s) is not None:
            return cache.get(s)

        tmp_res = []
        for i in range(len(s)):
            word = s[:i+1]
            if word in word_set:
                # recursion and back tracking
                # self.recursion(s[i+1:], word_set, res, [word] + answer, cache)
                tmp = self.recursion(s[i+1:], word_set, cache)
                # a string may have more than one combination of words list
                # so, the result is a 2d list, one inner list is one answer
                for item in tmp:
                    tmp_item = [word] + item
                    tmp_res.append(tmp_item)

        cache[s] = tmp_res
        # todo: attention this return when memorize
        return tmp_res

    def recursion_basic(self, s, word_set, res, answer):
        """
        basic recursion version, final result is in res
        :param s: string to check
        :param word_set: set of all possible words
        :param res: result list
        :param answer: an possible answer
        :return:
        """
        if not s:
            res.append(answer)
            return True  # end

        for i in range(len(s)):
            word = s[:i+1]
            if word in word_set:
                # recursion and back tracking
                # self.recursion(s[i+1:], word_set, res, [word] + answer)
                self.recursion_basic(s[i+1:], word_set, res, answer + [word])

    def recursion_basic_1(self, s, word_set):
        """
        basic recursion version
        :param s: string to check
        :param word_set: set of all possible words
        :return:
        """
        # todo: compare with recursion_basic()
        # attention this kind of return result,
        # and the diff between this and basic version where res is a global var
        if not s:
            return [[], ]  # end

        res = []
        for i in range(len(s)):
            word = s[:i+1]
            if word in word_set:
                # recursion and back tracking
                # self.recursion(s[i+1:], word_set, res, [word] + answer)
                tmp = self.recursion_basic_1(s[i+1:], word_set)
                for item in tmp:
                    res.append([word] + item)
        return res

    def format_res(self, data):
        res = []
        for answer in data:
            tmp = " ".join(answer)
            res.append(tmp)
        return res


if __name__ == "__main__":
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(Solution().wordBreak(s, wordDict))

    # todo: think again about return res, and modify global var when encounter stop condition

