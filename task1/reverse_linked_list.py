from linked_list import LinkedList

class ReverseLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def reverse_linked_list(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

