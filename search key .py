class Solution:
    def searchKey(self, n, head, key):
        current = head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False