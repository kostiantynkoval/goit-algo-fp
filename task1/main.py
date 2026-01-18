from reverse_linked_list import ReverseLinkedList
from merge_sort import SortableLinkedList
from merge_sorted_linked_lists import merge_sorted_linked_lists


def main():
    # Reverse linked list
    rll = ReverseLinkedList()
    rll + 1
    rll + 2
    rll + 3
    rll + 4
    rll + 5
    rll + 6
    rll + 7
    rll + 8
    rll + 9
    print("**** Before reverse:", end=" ")
    rll.print_list()
    rll.reverse_linked_list()
    print("***** After reverse:", end=" ")
    rll.print_list()

    # Merge sort
    ll = SortableLinkedList()
    ll + 10
    ll + 8
    ll + 30
    ll + 19
    ll - 4
    ll - 5
    print("**** Before sorting:", end=" ")
    ll.print_list()
    ll.head = ll.merge_sort(ll.head)
    print("***** After sorting:", end=" ")
    ll.print_list()

    # Merge two sorted linked lists
    ll1 = SortableLinkedList()
    ll1 + 1
    ll1 + 5
    ll1 + 9
    ll1 + 12
    ll1 + 15
    ll2 = SortableLinkedList()
    ll2 + 10
    ll2 + 11
    ll2 + 16
    ll2 + 17
    ll2 + 18
    c = merge_sorted_linked_lists(ll1, ll2)
    print("Merged linked list:", end=" ")
    c.print_list()


if __name__ == '__main__':
    main()
