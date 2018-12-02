#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return self.quick_ans(s)
        return self.order_dict(s)

    def quick_ans(self, s):
        from collections import Counter
        s_counter = Counter(s)

        kv_list = [(k,v) for k, v in s_counter.iteritems()]
        kv_list.sort(key=lambda x: x[1], reverse=True)

        res = ""
        for k, v in kv_list:
            tmp = k*v
            res += tmp

        return res

    def order_dict(self, s):
        from collections import Counter
        from collections import OrderedDict
        s_counter = Counter(s)
        s_dict = OrderedDict(sorted(s_counter.iteritems(),
                                    key=lambda x:x[1], reverse=True))

        res = ""
        for k, v in s_dict.iteritems():
            res += k*v
        return res


if __name__ == "__main__":
    test_s = "tree"
    print(Solution().frequencySort(test_s))

