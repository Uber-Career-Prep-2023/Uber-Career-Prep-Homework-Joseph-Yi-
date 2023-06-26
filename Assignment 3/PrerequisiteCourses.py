# Graph - DFS

# Time complexity is O(n + m)
# creating graph requires O(m) time. The dfs
# will take worst O(n) time. The two in succeession take O(n + m)

# Space complexity is O(n)
# The graph stores dependent on the number of courses that exist.

# This took me 28 min

# let n be the number of courses and m be the number of prereq relationships
def PrerequisiteCourses(courses, prerequisites):

    prereq_dict = {course: set() for course in courses}
    for course, prereq in prerequisites.items():
        prereq_dict[course] = set(prereq)
    
    valid_order = []
    visited = set()

    def dfs(course):

        if course in visited:
            return False
        if course in valid_order:
            return True

        visited.add(course)

        for prereq in prereq_dict[course]:
            if not dfs(prereq):
                return False

        visited.remove(course)
        valid_order.append(course)
        return True

    for course in courses:
        if not dfs(course):
            return []

    valid_order.reverse()
    return valid_order


courses = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
prerequisites = {
    "Data Structures": ["Intro to Programming"],
    "Advanced Algorithms": ["Data Structures"],
    "Operating Systems": ["Advanced Algorithms"],
    "Databases": ["Advanced Algorithms"]
}

print(PrerequisiteCourses(courses, prerequisites))


