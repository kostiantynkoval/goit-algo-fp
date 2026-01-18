from utils.draw_bynary_tree import draw_tree, Node
from collections import deque
from matplotlib import cm


# This file needs to be run from the root directory of the project `goit-algo-fp`
# Correct command to run this file from the terminal:
# python3 -m task5.main


def heap_to_tree_bfs(heap):
    if not heap:
        return None

    counter = 0
    root = Node(heap[0], cm.inferno(0.2))
    queue = deque([(root, 0)])

    while queue:
        node, index = queue.popleft()

        left_index = 2 * index + 1
        right_index = 2 * index + 2


        if left_index < len(heap):
            counter += 1
            node.left = Node(heap[left_index], cm.inferno(0.2 + (counter / len(heap) * 0.7 )))
            queue.append((node.left, left_index))

        if right_index < len(heap):
            counter += 1
            node.right = Node(heap[right_index], cm.inferno(0.2 + (counter / len(heap) * 0.7 )))
            queue.append((node.right, right_index))

    return root


def heap_to_tree_dfs(heap):
    n = len(heap)

    if n == 0:
        return None, []

    counter = 0
    root = Node(heap[0], cm.inferno(0.2))
    stack = []
    right_idx = 2 * 0 + 2
    left_idx = 2 * 0 + 1

    if right_idx < n:
        stack.append((right_idx, root, False))
    if left_idx < n:
        stack.append((left_idx, root, True))

    while stack:
        idx, parent, is_left = stack.pop()
        counter += 1
        node = Node(heap[idx], cm.inferno(0.2 + (counter / len(heap) * 0.7 )))
        if is_left:
            parent.left = node
        else:
            parent.right = node

        right_idx = 2 * idx + 2
        left_idx = 2 * idx + 1

        if right_idx < n:
            stack.append((right_idx, node, False))
        if left_idx < n:
            stack.append((left_idx, node, True))

    return root


if __name__ == "__main__":
    heap = [1, 4, 7, 8, 9, 10, 13, 15,16,17,18,20,22,23]
    # root = heap_to_tree_bfs(heap)
    root = heap_to_tree_dfs(heap)

    draw_tree(root)