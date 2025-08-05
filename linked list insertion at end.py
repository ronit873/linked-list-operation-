class Solution:
    def insertAtEnd(self, head, x):
        new_node = Node(x)
        

        if not head:
            return new_node
        
        current = head
        while current.next:
            current = current.next
        
        current.next = new_node
        
        return head