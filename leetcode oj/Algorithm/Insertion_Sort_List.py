## Insertion Sort List
"""
Sort a linked list using insertion sort
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @param head, a ListNode
# @return a ListNode
def insertionSortList(head):
    if not head:
        return head
    fh = ListNode(0)
    fh.next = head
    current = head
    while current.next:
        if current.next.val < current.val:
            previous = fh
            while previous.next.val < current.next.val:
                previous = previous.next
            t = current.next
            current.next = t.next
            t.next = previous.next
            previous.next = t
        else:
            current = current.next
    return fh.next
