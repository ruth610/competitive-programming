# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        incoming = [0 for _ in range(n)]
        queue = deque()
        for f_node,l_node in edges:
            graph[f_node].append(l_node)
            incoming[l_node] += 1
        for i,edge in enumerate(incoming):
            if edge == 0:
                queue.append(i)
        print(graph)
        res = [set() for _ in range(n)]
        while queue:
            zero_degree_edge = queue.popleft()
            nei = graph[zero_degree_edge]
            for edge in nei:
                res[edge].add(zero_degree_edge)
                res[edge].update(res[zero_degree_edge])
                incoming[edge] -= 1
                if incoming[edge] == 0:
                    queue.append(edge)
        return [sorted(list(ans)) for ans in res]
