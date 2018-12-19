#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.



Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.


Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
"""


class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # return self.ans(A)
        return self.ans_1(A)

    def ans(self, A):
        odd = []
        even = []

        for item in A:
            if item % 2 == 0:
                odd.append(item)
            else:
                even.append(item)

        res = []
        for odd_item, even_item in zip(odd, even):
            res.append(odd_item)
            res.append(even_item)

        return res

    def ans_1(self, A):
        """
        2 pointers, one point to odd and the other point to even
        :param A:
        :return:
        """
        odd = 0
        even = 0

        res = []
        while odd < len(A) and even < len(A):
            # find odd
            while A[odd] % 2 != 0:
                odd += 1
            res.append(A[odd])
            odd += 1

            # find even
            while A[even] % 2 == 0:
                even += 1
            res.append(A[even])
            even += 1

        return res


if __name__ == "__main__":
    test_data = [4,2,1,3]
    print(Solution().sortArrayByParityII(test_data))
    print(Solution().ans_1(test_data))
