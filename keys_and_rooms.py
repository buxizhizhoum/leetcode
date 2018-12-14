#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room.

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0).

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:

Input: [[1],[2],[3],[]]
Output: true
Explanation:
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.
Example 2:

Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.
Note:

1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
The number of keys in all rooms combined is at most 3000.
"""
import bisect


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        # visited = [0]
        # return self.dfs(rooms, 0, visited)
        # visited = {0: True}
        # return self.dfs_optimize(rooms, 0, visited)
        visited = [False for _ in range(len(rooms))]
        visited[0] = True
        # return self.dfs_optimize_refer_solution(rooms, 0, visited)
        return self.dfs_optimize_new(rooms, 0, visited)

    def dfs(self, rooms, start, visited):
        # if all rooms are visited
        if visited == range(len(rooms)):
            return True

        # get keys in current room
        keys = rooms[start]
        for key in keys:
            if start == key:
                # this if is just an optimization
                # if a room store its own key, continue next loop
                continue

            if key not in visited:
                bisect.insort(visited, key)
                # todo: attention return method in recursion
                res = self.dfs(rooms, key, visited)
                if res is True:
                    return res

        # todo: attention return method in recursion
        return False

    # todo: does it better to buffer visited with dict
    def dfs_optimize(self, rooms, start, visited):
        # if all rooms are visited
        if len(visited.keys()) == len(rooms) and all(visited.values()):
            return True

        # get keys in current room
        keys = rooms[start]
        for key in keys:
            if start == key:
                # this if is just an optimization
                # if a room store its own key, continue next loop
                continue

            # if not visited, visit it
            if not visited.get(key):
                # bisect.insort(visited, key)
                visited[key] = True

                # todo: attention return method in recursion
                res = self.dfs_optimize(rooms, key, visited)
                if res is True:
                    return True

        # todo: attention return method in recursion
        return False

    def dfs_optimize_refer_solution(self, rooms, start, visited):
        # if all rooms are visited
        if len(visited) == len(rooms) and all(visited):
            return True

        # get keys in current room
        keys = rooms[start]
        for key in keys:
            if start == key:
                # this if is just an optimization
                # if a room store its own key, continue next loop
                continue

            # if not visited, visit it
            if not visited[key]:
                # bisect.insort(visited, key)
                visited[key] = True

                # todo: attention return method in recursion
                res = self.dfs_optimize_refer_solution(rooms, key, visited)
                if res is True:
                    return True

        # todo: attention return method in recursion
        return False

    def dfs_optimize_new(self, rooms, start, visited):
        # get keys in current room
        keys = rooms[start]
        for key in keys:
            if start == key:
                # this if is just an optimization
                # if a room store its own key, continue next loop
                continue

            # if not visited, visit it
            if not visited[key]:
                # bisect.insort(visited, key)
                visited[key] = True

                # todo: attention return method in recursion
                self.dfs_optimize_new(rooms, key, visited)

        # todo: attention return method in recursion
        return all(visited)


if __name__ == "__main__":
    test_rooms = [[1],[2],[3],[]]
    # test_rooms = [[1,3],[3,0,1],[2],[0]]
    # test_rooms = [[2,3],[],[2],[1,3,1]]
    print(Solution().canVisitAllRooms(test_rooms))

    # try visit dict

