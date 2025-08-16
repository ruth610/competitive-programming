# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [-1 for i in range(len(edges) + 1)]
        def find(x):
            if parent[x] < 0:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(a,b):
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return False
            if root_a > root_b:
                root_a , root_b = root_b, root_a
            
            parent[root_a] += parent[root_b]
            parent[root_b] = root_a
            return True
        for u , v in edges:
            if not union(u,v):
                return [u,v]

        
            
