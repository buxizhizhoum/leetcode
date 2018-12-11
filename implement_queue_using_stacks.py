#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""


class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.stack2:
            return self.stack2.pop()

        else:
            # move data in stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())

            if self.stack2:
                return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stack2:
            return self.stack2[-1]
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

            if self.stack2:
                return self.stack2[-1]
        return None

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if not self.stack1 and not self.stack2:
            return True
        return False


if __name__ == "__main__":
    # Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()
    for i in range(5):
        obj.push(i)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
    for i in range(5, 10):
        obj.push(i)

    for i in range(10):
        print(obj.peek())
        obj.pop()



