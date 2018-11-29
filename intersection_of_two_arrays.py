#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return self.two_pointer(nums1, nums2)
        # return self.counter(nums1, nums2)

    def counter(self, nums1, nums2):
        from collections import Counter

        count = Counter(nums1)

        res = []
        for item in nums2:
            tmp = count.get(item)
            if tmp is not None and tmp > 0:
                res.append(item)
                count[item] -= 1

        return res

    def two_pointer(self, nums1, nums2):
        nums1.sort()
        nums2.sort()

        p_1 = 0
        p_2 = 0

        res = []
        cur_val = None
        while p_1 < len(nums1) and p_2 < len(nums2):
            if nums1[p_1] < nums2[p_2]:
                p_1 += 1
                continue

            if nums1[p_1] > nums2[p_2]:
                p_2 += 1
                continue

            if cur_val != nums1[p_1]:
                res.append(nums1[p_1])
                cur_val = nums1[p_1]
            p_1 += 1
            p_2 += 1

        return res


if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    # print(Solution().counter(nums1, nums2))
    print(Solution().two_pointer(nums1, nums2))



