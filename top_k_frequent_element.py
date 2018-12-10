#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # return self.ans_pq(nums, k)
        return self.ans_heap(nums, k)

    def ans_pq(self, nums, k):
        from Queue import PriorityQueue
        from collections import Counter

        queue = PriorityQueue()

        if k <= 0:
            return

        counter = Counter(nums)
        for item, freq in counter.iteritems():
            if queue.qsize() < k:
                queue.put((freq, item))
            else:
                top = queue.get()
                if top[0] > freq:
                    queue.put(top)
                else:
                    queue.put((freq, item))

        # extract from priority queue
        res = []
        while not queue.empty():
            top = queue.get()
            res.append(top[1])
        return res

    def ans_heap(self, nums, k):
        import heapq
        from collections import Counter

        pq = []

        counter = Counter(nums)
        for num, freq in counter.items():
            if len(pq) < k:
                heapq.heappush(pq, (freq, num))
            else:
                top = pq[0]  # top item
                # top[0] is freq of top item
                if top[0] < freq:
                    heapq.heappop(pq)
                    heapq.heappush(pq, (freq, num))
        # extract pq
        res = []
        while pq:
            top = heapq.heappop(pq)
            res.append(top[1])

        return res


if __name__ == "__main__":
    test_nums = [1,1,1,2,2,3,3,3]
    k = 2
    print(Solution().ans_heap(test_nums, k))


