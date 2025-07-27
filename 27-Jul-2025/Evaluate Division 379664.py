# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1 / value

        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if end in graph[start]:
                return graph[start][end]
            visited.add(start)

            for neighbor, val in graph[start].items():
                if neighbor not in visited:
                    temp = dfs(neighbor, end, visited)
                    if temp != -1.0:
                        return temp * val
            return -1.0

        res = []
        for v1, v2 in queries:
            visited = set()
            res.append(dfs(v1, v2, visited))

        return res
        