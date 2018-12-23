#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
"""
# the answer is a trie


class WordDictionary(object):
    class Node(object):
        def __init__(self, isword=False):
            self.isword = isword
            self.next = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for char in word:
            if cur.next.get(char) is None:
                cur.next[char] = self.Node()
            # get next node
            cur = cur.next[char]

        cur.isword = True

    def search(self, word):
        """
        Returns if the word is in the data structure.
        A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        # start from root node
        cur = self.root
        return self._search(cur, word)

    def _search(self, cur, word):
        if not word:
            # if encounter end, check whether it is marked as end of a word
            return cur.isword

        char = word[0]

        if char != ".":
            if cur.next.get(char) is None:
                return False
            # search next node
            return self._search(cur.next[char], word[1:])
        else:
            # check all node in cur.next
            for _, next_node in cur.next.items():
                tmp_res = self._search(next_node, word[1:])
                # if founded, return
                if tmp_res is True:
                    return True
            return False


if __name__ == "__main__":
    # Your WordDictionary object will be instantiated and called as such:
    obj = WordDictionary()
    obj.addWord("apple")
    # param_2 = obj.search("apple")
    param_2 = obj.search("app")
    print(param_2)






