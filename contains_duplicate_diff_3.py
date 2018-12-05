#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an array of integers, find out whether there are two distinct indices
i and j in the array such that the absolute difference between
nums[i] and nums[j] is at most t and the absolute difference between i and j is
at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
"""


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # return self.math_trick(nums, k, t)
        return self.math_trick_1(nums, k, t)

    def first_ans(self, nums, k, t):
        if len(nums) < 2:
            return False

        if k == 0:
            return False

        window = {}
        # initialize the window with size of k
        for i in range(k):
            # | new_num - num_in_window | <= t  =>
            # -t + new <= num_in_window <= new + t
            # todo: to find num in dict, so the condition should be transformed to find a certain number in dict
            for close_num in xrange(nums[i] - t, nums[i] + t + 1):
                if close_num in window:
                    return True
            window[nums[i]] = i

        l = 0
        r = l + k
        while r + 1 < len(nums):
            window.pop(nums[l])

            for close_num in xrange(nums[r+1] - t, nums[r+1] + t + 1):
                if close_num in window:
                    return True
            window[nums[r]] = r
            r += 1
            l += 1

        return False

    def math_trick(self, nums, k, t):
        if len(nums) < 2:
            return False

        if k == 0:
            return False

        from collections import OrderedDict
        window = OrderedDict()
        # initialize the window with size of k
        for i in range(k):
            # | new_num - num_in_window | <= t  =>
            # -t + new <= num_in_window <= new + t
            # todo: to find num in dict, so the condition should be transformed to find a certain number in dict
            # todo: Attention, math trick, shirnk xrange
            # => new//t - 1 <= num_in_window //t <= new//t + 1
            key = nums[i] if not t else nums[i]//t
            for close_key in (key - 1, key, key + 1):
                if close_key in window and abs(nums[i] - nums[window[close_key]]) <= t:
                    return True
            window[key] = i

        l = 0
        r = l + k
        while r < len(nums):
            key = nums[r] // t if t else nums[r]
            for close_key in (key - 1, key, key + 1):
                if close_key in window and abs(nums[r] - nums[window[close_key]]) <= t:
                    return True
            window[key] = r

            if len(window) >= k:
                window.popitem(last=False)

            r += 1
            l += 1

        return False

    def math_trick_1(self, nums, k, t):
        if len(nums) < 2:
            return False

        if k == 0:
            return False

        # easy to maintain window with OrderedDict
        from collections import OrderedDict
        window = OrderedDict()

        r = 0
        while r < len(nums):
            # | new_num - num_in_window | <= t  =>
            # -t + new <= num_in_window <= new + t
            # todo: to find num in dict, so the condition should be transformed to find a certain number in dict
            # todo: Attention, math trick, shirnk xrange
            # => new//t - 1 <= num_in_window //t <= new//t + 1
            key = nums[r] // t if t else nums[r]
            for close_key in (key - 1, key, key + 1):
                if close_key in window:
                    # get index of close num
                    close_num_index = window[close_key]
                    if abs(nums[r] - nums[close_num_index]) <= t:
                        return True

            if len(window) >= k:
                window.popitem(last=False)

            window[key] = r
            r += 1

        return False


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    k = 3
    t = 0
    nums = [1, 5, 9, 1, 5, 9]
    k = 2
    t = 3
    # nums = [-3, 3]
    # k = 2
    # t = 4
    # nums = [1, 2]
    # k = 0
    # t = 1
    # nums = [0, 2147483647]
    # k = 1
    # t = 2147483647
    # nums = [1, 0, 1, 1]
    # k = 1
    # t = 2
    #
    nums = [1, 3, 6, 2]
    k = 1
    t = 2

    print(Solution().containsNearbyAlmostDuplicate(nums, k, t))








