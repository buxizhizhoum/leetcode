#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minimum = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.minimum:
            cur_min = min(x, self.minimum[-1])
        else:
            cur_min = x
        self.minimum.append(cur_min)

    def pop(self):
        """
        :rtype: void
        """
        self.minimum.pop()
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.minimum[-1]
        return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)

    print(min_stack.getMin())

    min_stack.pop()
    print(min_stack.getMin())

