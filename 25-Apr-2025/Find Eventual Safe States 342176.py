# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe_nodes = {}
        def dfs(t):
            if t in safe_nodes:
                return safe_nodes[t]
            safe_nodes[t] = False
            for nei in graph[t]:
                if not dfs(nei):
                    return False
            safe_nodes[t] = True
            return safe_nodes[t]
        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res