def deleteNode(head, x):

    if not head:
        return None

    if x == 1:
        return head.next

    current = head

    for _ in range(x - 2):
        if current is None:
            return head 
        current = current.next


    if current and current.next:
        current.next = current.next.next

    return head