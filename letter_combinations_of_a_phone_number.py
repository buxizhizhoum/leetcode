#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""


class Solution(object):
    letters = [" ", "", "abc", "def", "ghi",
               "jkl", "mno", "pqrs", "tuv", "wxyz"]
    res = []

    def letterCombinations(self, digits):
        """
        :type digits: str, eg. "235"
        :rtype: List[str]
        """
        if digits == "":
            return []
        self.find_combination(digits, 0, "")
        # self.find_combination_2(digits, len(digits) - 1, "")
        return self.res

    def find_combination(self, digits, index, cur_string):
        """
        find combination recursion

        index change from 0 to len(digits), the digit is processed
        from first char to the last one,
        so char from letter_str should be add at the end of cur_string

        "235"
        "2" + "35"
        "2" + "3" + "5"

        :param digits: a string contains digit, eg."235"
        :param index: int, index on char in string digits
        :param cur_string:
        :return:
        """
        if index == len(digits):
            self.res.append(cur_string)
            return

        letter_str_index = digits[index]  # a digit in type of str
        # get corresponding letters_str according to digit
        letter_str = self.letters[int(letter_str_index)]
        # another method
        # letter_str = self.letters[letter_str_index - "0"]
        # todo: Attention, last one did not recur and just return.
        # todo: Attention, cur_string + char is used to assemble string
        for char in letter_str:
            self.find_combination(digits, index + 1, cur_string + char)

    def find_combination_2(self, digits, index, cur_string):
        """
        find combination recursion
        :param digits: a string contains digit, eg."235"
        :param index: int, index on char in string digits
        :param cur_string:
        :return:
        """
        if index == -1:
            self.res.append(cur_string)
            return

        letter_str_index = digits[index]  # a digit in type of str
        # get corresponding letters_str according to digit
        letter_str = self.letters[int(letter_str_index)]
        # another method
        # letter_str = self.letters[letter_str_index - "0"]
        for char in letter_str:
            self.find_combination_2(digits, index - 1, char + cur_string)


if __name__ == "__main__":
    # print(Solution().letterCombinations("235"))
    print(Solution().letterCombinations("2"))
    # local test pass, leetcode not pass

    






