#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Determine whether an integer is a palindrome. An integer is a palindrome when
it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left,
it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        return self.ans(x)

    def ans(self, x):
        cache = []
        while x != 0:
            mod = x % 10
            x = x // 10

            cache.append(mod)

        # unnecessary
        cache.reverse()

        i, j = 0, len(cache) - 1
        while i < j:
            if cache[i] != cache[j]:
                return False

            i += 1
            j -= 1

        return True


if __name__ == "__main__":
    print(Solution().isPalindrome(121))



