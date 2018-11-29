#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""


class Solution(object):
    def intersect(self, nums1, nums2):
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
        while p_1 < len(nums1) and p_2 < len(nums2):
            if nums1[p_1] < nums2[p_2]:
                p_1 += 1
                continue

            if nums1[p_1] > nums2[p_2]:
                p_2 += 1
                continue

            # if nums1[p_1] == nums2[p_2]:
            res.append(nums1[p_1])
            p_1 += 1
            p_2 += 1
        return res


if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2]
    # print(Solution().counter(nums1, nums2))
    print(Solution().two_pointer(nums1, nums2))



