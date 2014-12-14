class MinStack:
    def __init__(self):
        self.data = []
        self.min_data = []
    
    # @param x, an integer
    # @Push element x onto stack
    def push(self, x):
        self.data.append(x)
        ## min value stack
        if len(self.min_data) == 0 or x <= self.min_data[-1]:
            self.min_data.append(x)

    # @Removes the element on top of the stack
    def pop(self):
        item = self.data.pop()
        if self.min_data and item == self.min_data[-1]:
            self.min_data.pop()

    # @Get the top element
    def top(self):
        if len(self.data) > 0:
            return self.data[-1]
        

    # @Retrive the minimum element in the stack
    def getMin(self):
        if len(self.min_data) > 0:
            return self.min_data[-1]

    def isEmpty(self):
        return self.data == []

    def size(self):
        return len(self.data)
