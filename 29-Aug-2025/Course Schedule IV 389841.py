# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # prerequisites.sort(key=lambda x:x[1])
        # print(prerequisites)
        graph = [[] for _ in range(numCourses)]
        for u,v in prerequisites:
            graph[u].append(v)
        prereq_sets = [set() for _ in range(numCourses)]

        def dfs(course):
            if prereq_sets[course]:
                return prereq_sets[course]
            for nxt in graph[course]:
                prereq_sets[course].add(nxt)
                prereq_sets[course] |= dfs(nxt)
            return prereq_sets[course]

        # build all prerequisite sets
        for c in range(numCourses):
            dfs(c)

        # answer queries
        return [v in prereq_sets[u] for u, v in queries]
            
        