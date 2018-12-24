#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an array nums of n integers, are there elements a, b, c in nums
such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
import time


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # return self.dict_ans(nums)
        # return self.sort_ans(nums)
        return self.dict_ans_2(nums)

    def dict_ans(self, nums):
        buffer_dict = {}
        t0 = time.time()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum_ = nums[i] + nums[j]
                if buffer_dict.get(sum_) is None:
                    buffer_dict[sum_] = [(i, j)]
                else:
                    buffer_dict[sum_].append((i, j))
        print("dict:", time.time() - t0)

        res = set()
        t1 = time.time()
        for i in range(len(nums)):
            # target = 0 - nums[i]
            target = - nums[i]
            # [(0, 3), (1, 2), (3, 4)]
            indexes = buffer_dict.get(target, [])
            # if indexes is not None:
            for index in indexes:
                if i not in index:
                    tmp = sorted([nums[i], nums[index[0]], nums[index[1]]])
                    res.add(tuple(tmp))
        print("res:", time.time() - t1)

        return list([list(item) for item in res])

    def sort_ans(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for index, num in enumerate(nums[:-2]):
            # print index
            target = 0 - num
            l = index + 1
            r = len(nums) - 1
            while l < r:
                # print "l", index, l
                if nums[l] + nums[r] == target:
                    tmp = tuple([nums[index], nums[l], nums[r]])
                    res.add(tmp)
                    # update l, r
                    if (l + 1) < r and nums[l] == nums[l + 1]:
                        l += 1
                    elif (r - 1) > l and nums[r] == nums[r - 1]:
                        r -= 1
                    else:
                        # move l or r with as less influence to sum as possible
                        # do not count a same answer two times
                        l += 1
                        r -= 1  # why add this line also works, duplicate not count
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return list(map(list, res))

    def dict_ans_2(self, nums):
        if len(nums) < 3:
            return []
        # dict buffer last layer
        buffer_dict = {}
        for index, num in enumerate(nums):
            if num not in buffer_dict:
                buffer_dict[num] = [index]
            else:
                buffer_dict[num].append(index)

        res = set()
        t0 = time.time()
        for i, num in enumerate(nums):
            for j, v in enumerate(nums[i + 1:], start=i+1):
                diff = 0 - (num + v)
                indexes = buffer_dict.get(diff)
                if not indexes:
                    continue
                for index in indexes:
                    # one element should not be used two times
                    if i != index and j != index:
                        res.add(tuple(sorted([num, v, diff])))
        print(time.time() - t0)
        return list(map(list, res))


if __name__ == "__main__":
    test_input = [-1, 0, 1, 2, -1, -4]
    test_input = [0,0]
    test_input = [1,2,-2,-1]
    print(len(test_input))
    print(Solution().threeSum(test_input))

    # todo: time limit exceeded



