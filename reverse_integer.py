#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_x = str(abs(x))
        tmp_res = str_x[::-1]

        res = int(tmp_res) if x >= 0 else -int(tmp_res)
        res = res if abs(res) <= 2147483647 else 0

        return int(res)


if __name__ == "__main__":
    solution = Solution()
    print solution.reverse(132)
    print solution.reverse(130)
    print solution.reverse(-123)
    print solution.reverse(-2147483648)