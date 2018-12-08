#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            # if char is left part
            if char in ("(", "[", "{"):
                stack.append(char)
            # if char is right part, pop a char from stack
            else:
                # ensure stack size is larger than 0 when pop
                if len(stack) > 0:
                    top = stack.pop()
                    # check whether char and top of stack is match
                    if not self.match(char, top):
                        return False
                else:
                    return False
        # if stack size != 0, means left part is more than right part
        if len(stack) != 0:
            return False
        return True

    def match(self, char, top):
        # if top in (")", "]", "}"):
        if char == ")" and top == "(":
            return True
        elif char == "]" and top == "[":
            return True
        elif char == "}" and top == "{":
            return True
        else:
            return False
        # else:
        #     return False


if __name__ == "__main__":
    test = "([)]"
    test = "()"
    print(Solution().isValid(test))

