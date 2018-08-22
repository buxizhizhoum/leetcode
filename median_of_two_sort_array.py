#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_array = self.merge(nums1, nums2)
        length = len(merged_array)
        mid_index = length // 2
        if mid_index == 0:
            return merged_array[0]

        if length % 2 == 0:
            res = (merged_array[mid_index - 1] + merged_array[mid_index]) / 2.0
        else:
            res = merged_array[mid_index]
        return res

    @staticmethod
    def merge(l1, l2):
        i, j = 0, 0
        res = []
        while i < len(l1) and j < len(l2):
            if l1[i] <= l2[j]:
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1

        if i < len(l1):
            res.extend(l1[i:])
        if j < len(l2):
            res.extend(l2[j:])

        return res


if __name__ == "__main__":
    l_1 = [1, 2, 5, 7, 9]
    l_2 = [2, 3, 3, 6, 8]

    s = Solution()
    print(s.findMedianSortedArrays(l_1, l_2))



