#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Example 1:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Example 2:

Input: version1 = "1.0.1", version2 = "1"
Output: 1
Example 3:

Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
"""


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version_1 = version1.split(".")
        version_2 = version2.split(".")

        i = 0
        while i < len(version_1) and i < len(version_2):
            if int(version_1[i]) > int(version_2[i]):
                return 1
            elif int(version_1[i]) < int(version_2[i]):
                return -1
            i += 1

        # length equals, if not return in loop, it means equal
        if i == len(version_1) and i == len(version_2):
            return 0
        # version_1 is shorter
        elif i == len(version_1):
            # check whether rest of version_2 is all 0
            if all([True if int(item) == 0 else False for item in version_2[i:]]):
                # rest is all zero, ==
                return 0
            return -1
        # version 2 is shorter
        elif i == len(version_2):
            # check whether rest of version_1 is all 0
            tmp = [True if int(item) == 0 else False for item in version_1[i:]]
            if all([True if int(item) == 0 else False for item in version_1[i:]]):
                # rest of version_1 is all zero
                return 0
            return 1

        return 0


if __name__ == "__main__":
    version1 = "7.5.2.4"
    version2 = "7.5.3"

    version1 = "01"
    version2 = "1"

    version1 = "1.0.0.0.0.0"
    version2 = "1"

    version1 = "1"
    version2 = "1.1"
    print(Solution().compareVersion(version1, version2))



