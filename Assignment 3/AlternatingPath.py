# Graph - BFS

# Time complexity is O(V + E)
# The bfs visits each vertex and edge at least once

# Space Complexity is O(V)
# the graph stores data depedent on the number of vertices.

# this took me 29 min

from collections import deque

def AlternatingPath(origin, destination, graph):
    # Initialize a queue for BFS and a visited set
    queue = deque([(origin, 'blue'), (origin, 'red')])
    visited = set([(origin, 'blue'), (origin, 'red')])

    shortest_path = {origin: 0}

    while queue:
        node, color = queue.popleft()

        if node == destination:
            return shortest_path[node]

        # Checks neighbors
        for neighbor, edge_color in graph.get(node, []):

            # ensure altternating
            if edge_color != color:
                # calculates length
                new_length = shortest_path[node] + 1

                # Check if the neighbor has not been visited or a shorter path is found
                if (neighbor, edge_color) not in visited or new_length < shortest_path.get(neighbor, float('inf')):
                    shortest_path[neighbor] = new_length
                    visited.add((neighbor, edge_color))
                    queue.append((neighbor, edge_color))

    # No path
    return -1


graph = {
    'A': [('B', 'blue'), ('C', 'red'), ('D', 'red')],
    'B': [('D', 'blue'), ('E', 'blue')],
    'C': [('B', 'red')],
    'D': [('C', 'blue'), ('E', 'red')],
    'E': [('C', 'red')]
}

origin = 'E'
destination = 'D'
print(AlternatingPath(origin, destination, graph))