"""
WE PASSED
"""

from collections import deque

class MyStack(object):

    def __init__(self):
        self.stack = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.appendleft(x)

    def pop(self):
        """
        :rtype: int
        """
        pop_var = self.stack[0]
        self.stack.popleft()
        return pop_var

    def top(self):
        """
        :rtype: int
        """
        if not self.empty():
            return self.stack[0]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stack) == 0: return True 
        else: return False


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.top()
param_3 = obj.pop()
param_4 = obj.empty()
if param_2 == 2 and param_3 == 2 and param_4 == False:
    print('pass')
else:
    print('Fail')