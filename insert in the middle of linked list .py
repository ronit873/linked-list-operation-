class Solution:
    def insertInMiddle(self, head, x):
        new_node = Node(x)

        if not head:
            return new_node

        middle= head
        end= head

     
        while end.next and end.next.next:
            middle = middle.next
            end = end.next.next
        new_node.next = middle.next
        middle.next = new_node

        return head