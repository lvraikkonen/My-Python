class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(items)-1]

    def size(self):
        return len(self.items)

## reverse a string using stack
s = 'apple'
def revstring(mystr):
    s = Stack()
    for i in mystr:
        s.push(i)
    message = ""
    while not s.isEmpty():
        message += s.pop()
    return message
