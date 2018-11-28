#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return
        i, j = 0, 0
        while j < n and i < m:
            if nums1[i] >= nums2[j]:
                nums1.pop()  # pop 0 at the end of nums1 before insert into it.
                nums1.insert(i, nums2[j])
                i += 1  # insert will change index also, compensate it.
                m += 1  # insert will change length, modify it
                j += 1
            else:
                i += 1

        # if j < n-1
        for index in range(n-(n-j), n):
            nums1[i] = nums2[index]
            i += 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)



