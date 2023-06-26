# Graph - DFS
# This problem is basically counting the number fo connected components

# Space Complexity is O(V + E)
# The adjacency list will take up V + E space and
# the visited set is V space, thus the total space is V. So the 
# total space is 2V + E or just simply O(V + E)

# Time complexity is O(V + E)
# Building the adjacency list takes E time and the DFS
# at each vertex could take in worst case V + E time.
# This makes the total runtime be O(V + E)

# Approach
# I create an adjacency list with the edges given since the vertices dont matter. I then perform a simple 
# DFS on the graph marking all the visited in a set. I then count the number of 
# Connected components in the visisted set

# This took me 37 min

# Vertices are towns
# Edges are roads

from collections import defaultdict
def RoadNetworks(vertices, edges):

    # Create an adjacency list to represent the graph
    adjacency_list = defaultdict(list)
    for town1, town2 in edges:
        adjacency_list[town1].append(town2)
        adjacency_list[town2].append(town1)

    visited = set()

    # Simple visited DFS
    def dfs(vertex):
        visited.add(vertex)
        for neighbor in adjacency_list[vertex]:
            if neighbor not in visited:
                dfs(neighbor)

    count = 0


    for vertex in adjacency_list:
        if vertex not in visited:
            dfs(vertex)
            count += 1

    return count


print(RoadNetworks(["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"], 
[("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]))