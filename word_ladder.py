#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # res = self.recursion(beginWord, endWord, wordList, 0)
        cache = {}
        res = self.recursion(beginWord, endWord, wordList, 0, cache)
        res = 0 if res == float("inf") else res
        return res

    # def recursion(self, begin, end, word_list, length):
    #     # todo: how to return length, if it is only a ordinary variable
    #     if begin == end:
    #         # self.length_1 = length
    #         return length + 1
    #     # if there is no word in list and still not find end word, no path
    #     if len(word_list) == 0:
    #         return 0
    #
    #     res = float("inf")
    #     for index, word in enumerate(word_list):
    #         # if the word meet requirement
    #         if self.one_letter_diff(begin, word):
    #             new_len = self.recursion(word,
    #                                      end,
    #                                      word_list[:index]+word_list[index+1:],
    #                                      length + 1)
    #             res = min(res, new_len)
    #     return res

    def recursion(self, begin, end, word_list, length, cache):
        """
        time limit exceeded
        :param begin:
        :param end:
        :param word_list:
        :param length:
        :param cache:
        :return:
        """
        # print(begin, length, word_list)
        # todo: attention different with no cache version, length is incr from end
        if begin == end:
            # self.length_1 = length
            return 1
        # if there is no word in list and still not find end word, no path
        if len(word_list) == 0:
            return 0

        cache_res = cache.get(begin)
        if cache_res:
            # print("get res from cache: %s, %s" % (begin, cache_res))
            return cache_res
        res = float("inf")
        for index, word in enumerate(word_list):
            # if the word meet requirement
            if self.one_letter_diff(begin, word):
                new_len = self.recursion(word,
                                         end,
                                         word_list[:index]+word_list[index+1:],
                                         length + 1,
                                         cache)
                if new_len != 0:
                    new_len += 1
                    res = min(res, new_len)
        cache[begin] = res if res != float("inf") else None
        # todo: Attention, how to return length, if it is only a ordinary variable
        return res

    @staticmethod
    def one_letter_diff(word_1, word_2):
        """
        check whether the difference of two words is only one letter
        :param word_1:
        :param word_2:
        :return:
        """
        if len(word_1) != len(word_1):
            return False

        res = 0
        for i in range(len(word_1)):
            if word_1[i] != word_2[i]:
                res += 1

        return res == 1


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]

    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot", "dog"]

    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot", "cog", "dog", "tot", "hog", "hop", "pot", "dot"]

    beginWord = "qa"
    endWord = "sq"
    wordList = ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb",
                "kr", "ln",
                "tm", "le", "av", "sm", "ar", "ci", "ca", "br", "ti", "ba",
                "to", "ra",
                "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma",
                "re", "or",
                "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr",
                "nb", "yb",
                "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga", "li",
                "ha", "hz",
                "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an",
                "me", "mo",
                "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex",
                "pt", "io",
                "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq",
                "ye"]

    ladder_length = Solution().ladderLength(beginWord, endWord, wordList)
    print("result: %s" % ladder_length)





