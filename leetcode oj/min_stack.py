## Min Stack
"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

  push(x) -- Push element x onto stack.
  pop() -- Removes the element on top of the stack.
  top() -- Get the top element.
  getMin() -- Retrieve the minimum element in the stack.

"""
class MinStack:
    def __init__(self):
        self.data = []
        self.min_data = []

    def push(self,item):
        self.data.append(item)
        if not self.min_data or item <= self.min_data[-1]:
            self.min_data.append(item)

    def pop(self):
        if len(self.data) > 0:
            item = self.data.pop()
            if item == self.min_data[-1]:
                self.min_data.pop()

    def top(self):
        return self.data[-1]

    def getMin(self):
        return self.min_data[-1]

ms = MinStack()
ms.push(2)
ms.push(0)
ms.push(0)
ms.push(3)
print ms.data
