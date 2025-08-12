class Node:
    def __init__(self,val):
        self.next=None
        self.data=val


class Solution:
    def removeLoop(self, head):
        _set = set()
        removed = False
        prev = head
        while head:
            if head not in _set:
                _set.add(head)
                prev = head
                head = head.next
            else:
                prev.next = None
                removed = True
                break
        return removed