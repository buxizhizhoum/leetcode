#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
             received 3, 0, 6, 1, 5 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        return self.sort_version(citations)

    def sort_version(self, citations):
        if not citations:
            return 0
        citations.sort()
        length = len(citations)

        res = 0
        for i, num in enumerate(citations):
            if num >= length - i:
                res = max(res, length-i)

        return res


if __name__ == "__main__":
    test_citations = [3,0,6,1,5]
    print(Solution().hIndex(test_citations))

