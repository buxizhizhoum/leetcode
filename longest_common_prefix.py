#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        index = 0
        res = ""
        while index < len(strs) - 1:
            if index == 0:
                res = self.common_prefix(strs[index], strs[index + 1])
            else:
                res = self.common_prefix(res, strs[index+1])
            index += 1
        return res

    @staticmethod
    def common_prefix(s1, s2):
        l1 = list(s1)
        l2 = list(s2)

        i, j = 0, 0
        res = []
        while i < len(l1) and j < len(l2):
            if l1[i] == l2[j]:
                res.append(l1[i])
            else:
                break

            i += 1
            j += 1
        res_string = "".join(res) if res else ""
        return res_string


if __name__ == "__main__":
    # l = ["flower", "flow", "flight"]
    # l = ["dog","racecar","car"]

    l = ["aca", "cba"]
    solution = Solution()
    print(solution.longestCommonPrefix(l))
