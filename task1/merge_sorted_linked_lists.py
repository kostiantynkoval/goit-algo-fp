from requests import head

from linked_list import LinkedList, Node

def merge_sorted_linked_lists(list1: LinkedList, list2: LinkedList):
    dummy = Node(0)
    tail = dummy

    head1 = list1.head
    head2 = list2.head

    while head1 and head2:
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    tail.next = head1 if head1 else head2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list