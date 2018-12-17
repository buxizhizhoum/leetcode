#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Note:
N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <= 100.
"""
import collections
from Queue import PriorityQueue


class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = self.create_graph(times)
        # initialize all time of node to infinite
        # distance = {node: float("inf") for node in graph.keys()}

        # distance = {node: float("inf") for node in range(1, N+1)}
        # distance[K] = 0  # start node time is 0
        # self.dfs(graph, K, distance, 0)
        # return self.get_time(distance)

        cost = self.dj(graph, N, K)
        return self.get_time(cost)


    @staticmethod
    def create_graph(times):
        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append((u, v, w))

        return graph

    # def dfs(self, graph, start, distance, seconds):
    #     if distance[start] < seconds:
    #         # if time consumed from other node is larger than current time,
    #         # it means signal is already arrived
    #         return
    #
    #     # connected nodes
    #     neighbors = graph[start]
    #
    #     for _, node_to, node_w in neighbors:
    #         if distance[node_to] > distance[start] + node_w:
    #             # consumed time is the min time
    #             # todo: why not recover distance after dfs ? compare tree, recursion
    #             distance[node_to] = distance[start] + node_w
    #             self.dfs(graph, node_to, distance, distance[start] + node_w)

    def dfs(self, graph, start, distance, seconds):
        """
        depth first search, update distance of each node during searching
        :param graph:
        :param start: start node
        :param distance: dict used to cache time used before receiving signal
        :param seconds: time used before receiving signal
        :return:
        """
        if distance[start] < seconds:
            # if time consumed from other node is larger than current time,
            # it means signal is already arrived
            return

        # connected nodes
        neighbors = graph[start]
        # optimize, choose fast path first, if no optimize, time exceeded.
        neighbors.sort(key=lambda x:x[2])

        for _, node_to, node_w in neighbors:
            if distance[node_to] > distance[start] + node_w:
                # consumed time is the min time
                # todo: why not recover distance after dfs ? compare tree, recursion
                distance[node_to] = distance[start] + node_w
                self.dfs(graph, node_to, distance, distance[start] + node_w)

    def dj(self, graph, N, start):
        """
        迪杰斯特拉
        :param graph:
        :param N:
        :param start:
        :return:
        """
        # initialize time of all node to inf
        cost = {node: float("inf") for node in range(1, N + 1)}
        cost[start] = 0  # time from start to start is 0

        # cache whether a node is processed or not
        processed = {}
        # processed[start] = True

        queue = PriorityQueue()
        queue.put((0, start))  # node_id, node_weight
        while not queue.empty():
            # todo: Attention, a priority queue is used, and the node to
            # which signal arrives fastest is always the first one to process
            _, node_from = queue.get()

            neighbors = graph[node_from]

            for _, node_to, node_w in neighbors:
                # if a node is not processed, process it
                if not processed.get(node_to):
                    # if this route is faster, update consumed time
                    if cost[node_to] > cost[node_from] + node_w:
                        cost[node_to] = cost[node_from] + node_w
                    # no matter update cost or not, node_to should be put to q
                    queue.put((cost[node_from] + node_w, node_to))

            # after all neighbors have been processed, mark node as processed
            processed[node_from] = True

        return cost

    @staticmethod
    def get_time(distance):
        """
        get max time, it is the time consumed to send signal to all network
        :param distance:
        :return:
        """
        res = 0
        for node, w in distance.items():
            res = max(res, w)

        if res != float("inf"):
            return res
        return -1


if __name__ == "__main__":
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2

    # times = [[1, 2, 1], [2, 3, 7], [1, 3, 4], [2, 1, 2]]
    # n = 3
    # k = 2

    times = [[1, 3, 68], [1, 4, 20], [4, 1, 65], [3, 2, 74], [2, 1, 44],
             [3, 4, 61], [4, 3, 68], [3, 1, 26], [5, 1, 60], [5, 3, 3],
             [4, 5, 5], [2, 5, 36], [2, 3, 94], [1, 2, 0], [3, 5, 90],
             [2, 4, 28], [4, 2, 12], [5, 4, 52], [5, 2, 85], [1, 5, 42]]
    n = 5
    k = 4

    print(Solution().networkDelayTime(times, n, k))









