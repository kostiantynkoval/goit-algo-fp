from utils.draw_bynary_tree import draw_tree, Node

# This file needs to be run from the root directory of the project `goit-algo-fp`
# Correct command to run this file from the terminal:
# python3 -m task4.main

def heap_to_tree(heap, index=0):
    if index >= len(heap):
        return None

    node = Node(heap[index])

    node.left = heap_to_tree(heap, 2 * index + 1)
    node.right = heap_to_tree(heap, 2 * index + 2)

    return node


if __name__ == "__main__":
    heap = [1, 4, 7, 8, 9, 10, 13]
    root = heap_to_tree(heap)
    print(root)
    draw_tree(root)