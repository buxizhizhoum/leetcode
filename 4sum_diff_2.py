#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        return self.solve(A, B, C, D)

    def solve(self, A, B, C, D):
        dict_cd = {}
        for c in C:
            for d in D:
                if dict_cd.get(c+d) is None:
                    dict_cd[c+d] = 1
                else:
                    dict_cd[c+d] += 1

        res = 0
        for a in A:
            for b in B:
                if dict_cd.get(0 - a - b) is not None:
                    res += dict_cd[0 - a - b]

        return res

    def ab_cd(self, A, B, C, D):
        dict_ab = {}
        dict_cd = {}
        for a in A:
            for b in B:
                if dict_ab.get(a+b) is None:
                    dict_ab[a+b] = 1
                else:
                    dict_ab[a+b] += 1

        for c in C:
            for d in D:
                if dict_cd.get(c+d) is None:
                    dict_cd[c+d] = 1
                else:
                    dict_cd[c+d] += 1

        res = 0
        for ab, count_ab in dict_ab.iteritems():
            for cd, count_cd in dict_cd.iteritems():
                if ab + cd == 0:
                    res = res + count_ab * count_cd
        return res


if __name__ == "__main__":
    test_a = [1, 2]
    test_b = [-2, -1]
    test_c = [-1, 2]
    test_d = [0, 2]

    print(Solution().fourSumCount(test_a, test_b, test_c, test_d))


