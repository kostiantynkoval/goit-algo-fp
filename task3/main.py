import heapq

def dijkstra(graph, start):

    # Define distances dictionary and starting node
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Init binary heap
    queue = [(0, start)]

    while queue:
        # Get the smallest distance vertex in heap
        current_distance, current_vertex = heapq.heappop(queue)

        # Skip if current distance is greater than saved distance to current vertex
        if current_distance > distances[current_vertex]:
            continue

        # Update distances for all neighbors and add them to heap
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


if __name__ == '__main__':
    path_graph = {
        'A': [('B', 5), ('C', 1)],
        'B': [('A', 5), ('C', 2), ('D', 1)],
        'C': [('A', 1), ('B', 2), ('D', 4)],
        'D': [('B', 1), ('C', 4)]
    }

    result = dijkstra(path_graph, 'A')
    print(result)