# Graph - DFS

# Time complexity is O(V + E)
# The DFS visits each vertex and edge once

# Space complexity is O(V)
# the graph stores the information dependent on the number of vertices

# This took me 17 min
from collections import defaultdict, deque


def VacationDestinations(origin, k, destinations):
    graph = defaultdict(dict)

    for src, dest, time in destinations:
        graph[src][dest] = time
        graph[dest][src] = time

    queue = deque([(origin, 0)])
    visited = set([origin])
    count = 0

    while queue:
        city, travel_time = queue.popleft()

        if travel_time > k:
            break

        if travel_time <= k:
            count += 1

        for neighbor, time in graph[city].items():
            new_time = travel_time + time + 1  # Add 1 hour for stopover
            if new_time <= k and neighbor not in visited:
                queue.append((neighbor, new_time))
                visited.add(neighbor)

    return count - 1  # Exclude the origin city itself from the count


# Example usage:
origin_city = "New York"
max_travel_time = 5
destination_pairs = [
    ("Boston", "New York", 4),
    ("New York", "Philadelphia", 2),
    ("Boston", "Newport", 1.5),
    ("Washington, D.C.", "Harper's Ferry", 1),
    ("Boston", "Portland", 2.5),
    ("Philadelphia", "Washington, D.C.", 2.5)
]

num_destinations = VacationDestinations(origin_city, max_travel_time, destination_pairs)
print("Number of destinations within {} hours of {}: {}".format(max_travel_time, origin_city, num_destinations))
