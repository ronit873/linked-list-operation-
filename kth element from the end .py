class Solution:
    def getKthFromLast(self, head, k):
        front = head
        back = head
        

        for _ in range(k):
            if front is None:
                return -1  
            front = front.next

        while front is not None:
            front = front.next
            back = back.next

        return back.data