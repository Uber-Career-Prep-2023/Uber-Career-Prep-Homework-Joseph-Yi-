from collections import defaultdict
import copy


def build_graph(courses, prerequisites):
    graph = defaultdict(list)

    for course, prerequisite in prerequisites.items():
        graph[prerequisite].append(course)

    return graph


def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(course):
        visited.add(course)
        for neighbor in graph[course]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(course)

    for course in graph.keys():
        if course not in visited:
            dfs(course)

    return stack[::-1]


def course_order(courses, prerequisites):
    prerequisites_copy = copy.deepcopy(prerequisites)
    graph = build_graph(courses, prerequisites_copy)
    order = topological_sort(graph)
    return order


courses = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
prerequisites = {
    "Data Structures": "Intro to Programming",
    "Advanced Algorithms": "Data Structures",
    "Operating Systems": "Advanced Algorithms",
    "Databases": "Advanced Algorithms"
}

valid_order = course_order(courses, prerequisites)
print(valid_order)
