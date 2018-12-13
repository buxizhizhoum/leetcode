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
from Queue import Queue
import time


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        return self.ans(beginWord, endWord, wordList)

    def ans(self, begin_word, end_word, word_list):
        t0 = time.time()
        graph = self.create_graph(word_list)
        t1 = time.time()
        # self.show_graph(graph)
        print("create graph consumed %s seconds" % (t1 - t0,))
        res = self.bfs(graph, begin_word, end_word)
        print("bfs consumed %s seconds" % (time.time() - t1,))
        return res

    def create_graph(self, word_list):
        """
        create a graph based on the word_list
        :param word_list:
        :return:
        """
        graph = {word: [] for word in word_list}

        for index, word in enumerate(word_list):
            rest_words = word_list[:index] + word_list[index + 1:]

            # find word whose difference with current node is only one letter
            for rest_w in rest_words:
                if self.one_letter_diff(word, rest_w):
                    # append one letter diff word to .adjacent list
                    graph[word].append(rest_w)
        return graph

    @staticmethod
    def show_graph(graph):
        for node, linked_list in graph.iteritems():
            print("{}-> {}".format(node, linked_list))

    def bfs(self, graph, begin_word, end_word):
        visited = {}  # cache to record whether a node is visited
        order = {}  # cache to record the visit order of a node
        queue = Queue()

        # find words that is one letter diff with begin word
        for word, linked_list in graph.iteritems():
            if self.one_letter_diff(begin_word, word):
                queue.put(word)
                visited[word] = True
                order[word] = 2  # just an initial condition

        while not queue.empty():
            node = queue.get()

            if node == end_word:
                return order[node]

            # get nodes connected to cur node
            linked_words = graph[node]

            for word in linked_words:
                # if not visited before and only one letter diff, put to queue
                if not visited.get(word) and self.one_letter_diff(node, word):
                    queue.put(word)
                    visited[word] = True
                    order[word] = order[node] + 1

        return 0

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
    # todo: still time limit exceeded

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
                "kr", "ln", "tm", "le", "av", "sm", "ar", "ci", "ca", "br",
                "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr",
                "po", "fe", "ho", "ma", "re", "or", "rn", "au", "ur", "rh",
                "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb",
                "ge", "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz",
                "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an",
                "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi",
                "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr",
                "pa", "he", "lr", "sq", "ye"]

    ladder_length = Solution().ladderLength(beginWord, endWord, wordList)
    print("result: %s" % ladder_length)





