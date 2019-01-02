#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        return self.ans(nums)

    def ans(self, nums):
        if not nums:
            return []
        split_indexes = []
        # find split point
        start = 0
        for i in range(1, len(nums)):
            end = i - 1
            if nums[i] != nums[i-1] + 1:
                tmp = (start, end)
                split_indexes.append(tmp)
                start = i
        # add end
        split_indexes.append((start, len(nums)-1))

        # convert format
        res = []
        for start, end in split_indexes:
            if start == end:
                res.append(str(nums[start]))
            else:
                res.append("%s->%s" % (nums[start], nums[end]))

        return res


if __name__ == "__main__":
    test_nums = [0,2,3,4,6,8,9]
    print(Solution().summaryRanges(test_nums))



