from collections import deque

def AlternatingPath(origin, destination, graph):
    # Initialize a queue for BFS and a visited set
    queue = deque([(origin, 'blue'), (origin, 'red')])
    visited = set([(origin, 'blue'), (origin, 'red')])

    # Initialize a dictionary to store the shortest path length
    shortest_path = {origin: 0}

    # Perform BFS
    while queue:
        node, color = queue.popleft()

        # Check if the current node is the destination
        if node == destination:
            return shortest_path[node]

        # Explore neighboring nodes
        for neighbor, edge_color in graph.get(node, []):
            # Check if the edge color alternates
            if edge_color != color:
                # Calculate the length of the new path
                new_length = shortest_path[node] + 1

                # Check if the neighbor has not been visited or a shorter path is found
                if (neighbor, edge_color) not in visited or new_length < shortest_path.get(neighbor, float('inf')):
                    shortest_path[neighbor] = new_length
                    visited.add((neighbor, edge_color))
                    queue.append((neighbor, edge_color))

    # No alternating path found
    return -1


graph = {
    'A': [('B', 'blue'), ('C', 'red'), ('D', 'red')],
    'B': [('D', 'blue'), ('E', 'blue')],
    'C': [('B', 'red')],
    'D': [('C', 'blue'), ('E', 'red')],
    'E': [('C', 'red')]
}

origin = 'A'
destination = 'E'
print(AlternatingPath(origin, destination, graph))