from collections import deque

def adjacencySet(edges):
    graph = {}
    for edge in edges:
        node1, node2 = edge
        if node1 not in graph:
            graph[node1] = set()
        if node2 not in graph:
            graph[node2] = set()
        graph[node1].add(node2)
        if (node2, node1) in edges:
            graph[node2].add(node1)
    return graph

def bfs(target, graph):
    visited = set()
    queue = deque()
    queue.append(target)
    
    while queue:
        node = queue.popleft()
        if node == target:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    return False

def dfs(target, graph):
    visited = set()
    stack = [target]
    
    while stack:
        node = stack.pop()
        if node == target:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
    return False

def topologicalSort(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    queue = deque()
    for node in graph:
        if in_degree[node] == 0:
            queue.append(node)
    
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(result) != len(graph):
        # Graph contains a cycle, topological sort is not possible
        return []
    return result
