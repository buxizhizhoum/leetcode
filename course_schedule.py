#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.


For DFS, it will first visit a node, then one neighbor of it, then one neighbor of this neighbor... and so on.
If it meets a node which was visited in the current process of DFS visit, a cycle is detected and we will return false.
Otherwise it will start from another unvisited node and repeat this process till all the nodes have been visited.
Note that you should make two records: one is to record all the visited nodes and the other is to record
the visited nodes in the current DFS visit.

The code is as follows. We use a vector<bool> visited to record all the visited nodes
and another vector<bool> onpath to record the visited nodes of the current DFS visit.
Once the current visit is finished, we reset the onpath value of the starting node to false.

refer: https://leetcode.com/problems/course-schedule/discuss/58509/18-22-lines-C%2B%2B-BFSDFS-Solutions
"""


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True
        graph = self.create_graph(numCourses, prerequisites)

        return self.dfs(graph, numCourses)

    def create_graph(self, numCourses, prerequisites):
        """
        create graph
        :param numCourses:
        :param prerequisites:
        :return:
        """
        # it is a directed graph
        # {course: course_prerequisites, ...}
        graph = {i: set() for i in range(numCourses)}
        for edge in prerequisites:
            # add edge to graph, described with adjacent list
            # graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        return graph

    def dfs(self, graph, num_courses):
        # find whether there is a way to traverse all node
        # todo: Attention, it is a good thought to use to buffer
        visited = {}  # record all the visited nodes
        on_path = {}  # record visited nodes of current dfs
        # try every node as start
        for i in range(num_courses):
            if not visited.get(i) and self._dfs(graph, i, visited, on_path):
                return False

        return True

    def _dfs(self, graph, node, visited, on_path):
        """
        recursion to traverse graph from node,
        used to check whether there is a cycle
        :param graph:
        :param node:
        :return: True if there is a cycle, False if not
        """
        # todo: think again, this is not my answer...
        # i think the core thought is that if there is no cycle, it is possible
        if visited.get(node):
            # if node is already visited, there is a loop
            return False

        visited[node] = True
        on_path[node] = True

        neighbors = graph[node]

        for node_new in neighbors:
            if on_path.get(node_new) or self._dfs(graph, node_new, visited, on_path):
                return True  # there is cycle

        on_path[node] = False
        return False


if __name__ == "__main__":
    course_num = 2
    edges = [[1, 0]]
    # edges = [[1, 0], [0, 1]]

    course_num = 4
    # edges = [[1, 0], [2, 1], [3, 2]]
    # edges = [[1, 0], [2, 1], [3, 2], [1, 2]]
    edges = [[1, 0], [2, 1], [3, 2], [1, 3]]
    edges = [[1,0],[2,0],[3,1],[3,2]]

    # course_num = 3
    # edges = [[1, 0]]
    # course_num = 3
    # edges = [[0, 2], [1, 2], [2, 0]]
    # edges = [[1, 0], [1, 2], [0, 1]]
    # edges = [[0,1],[0,2],[1,0]]
    print(Solution().canFinish(course_num, edges))

    # give up, could not pass test
    # todo: check visiting, visited, not visited ans
    # https://leetcode.com/problems/course-schedule/discuss/58586/Python-20-lines-DFS-solution-sharing-with-explanation

    # def canFinish(self, numCourses, prerequisites):
    #     graph = [[] for _ in xrange(numCourses)]
    #     visit = [0 for _ in xrange(numCourses)]
    #     for x, y in prerequisites:
    #         graph[x].append(y)
    #
    #     def dfs(i):
    #         if visit[i] == -1:
    #             return False
    #         if visit[i] == 1:
    #             return True
    #         visit[i] = -1
    #         for j in graph[i]:
    #             if not dfs(j):
    #                 return False
    #         visit[i] = 1
    #         return True
    #
    #     for i in xrange(numCourses):
    #         if not dfs(i):
    #             return False
    #     return True
    # if node v has not been visited, then mark it as 0.
    # if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then their is a ring.
    # if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors.


