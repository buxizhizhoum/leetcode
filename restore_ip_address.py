#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        path = []
        self.restore_ip_2(s, res, path)
        return res

    def restore_ip(self, s, res, path):
        """
        :param s:
        :param res:
        :param path:
        :return:
        """
        if len(path) > 4:
            return

        if len(path) == 4 and len(s) == 0:
            # judge?
            res.append(".".join(path))
            return

        for i in range(1, min(4, len(s)+1)):
        # i = 1
        # while i <= min(3, len(s)):
            current_str = s[:i]
            if int(current_str) > 255 or (int(current_str[0]) == 0
                                          and len(current_str) == 1):
                continue
            # path.append(current_str)

            # if len(path) == 3 and i == len(s):
            #     res.append(".".join([path] + [current_str]))

            self.restore_ip(s[i:], res, path + [current_str])
            # path.pop()

    def restore_ip_2(self, s, res, path):
        # the 4 compare with path is due to ip address is composed of 4 parts.
        if len(path) > 4:
            return

        if len(path) == 4 and len(s) == 0:
            # judge? not needed, current_str is ensured between (0, 255)
            res.append(".".join(path))
            return

        # for循环用来回溯，当使用一个字符串作为开头不能解决问题，则再多选一个字符。
        # the 4 here is because every parts of ip address should be less than 4 digits
        # todo: Attention, This is optimization, line below also works, but cost more time
        for i in range(1, min(4, len(s) + 1)):  # 剪枝?
        # for i in range(1, len(s) + 1):
            current_str = s[:i]
            # if ip address part start with 0, it should be 0 only.
            if int(current_str) > 255 or (int(current_str[0]) == 0
                                          and len(current_str) > 1):
                continue

            self.restore_ip_2(s[i:], res, path + [current_str])
        return


if __name__ == "__main__":
    # input_str = "25525511135"
    input_str = "0000"
    print(Solution().restoreIpAddresses(input_str))




