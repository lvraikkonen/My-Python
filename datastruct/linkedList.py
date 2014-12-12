## Linked List Implementation
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

    def getValue(self):
        return self.val

    def getNext(self):
        return self.next

    def setValue(self,newValue):
        self.val = newValue

    def setNext(self,newNext):
        self.next = newNext

## test
#tmp = Node(93)
#tmp.getValue()

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        " add an item at the head of list "
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getValue() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        #search
        while not found:
            if current.getValue() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        #delete
        if prevoius == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
