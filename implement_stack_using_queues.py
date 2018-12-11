#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
"""


from Queue import Queue


class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue1.put(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        size = self.queue1.qsize()
        i = 0
        # put element except last element to queue
        while i < size - 1:
            element = self.queue1.get()
            self.queue2.put(element)
            i += 1

        res = self.queue1.get()

        # put element in queue2 back to queue1
        while not self.queue2.empty():
            self.queue1.put(self.queue2.get())

        return res

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        size = self.queue1.qsize()
        i = 0
        # put element except last element to queue
        while i < size - 1:
            self.queue2.put(self.queue1.get())
            i += 1

        res = self.queue1.get()
        self.queue2.put(res)

        # put element in queue2 back to queue1
        while not self.queue2.empty():
            self.queue1.put(self.queue2.get())

        return res

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self.queue1.empty() and self.queue2.empty():
            return True
        return False


if __name__ == "__main__":
    # Your MyStack object will be instantiated and called as such:
    obj = MyStack()
    for i in range(10):
        obj.push(i)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()

    while not obj.empty():
        print(obj.pop())


