# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [i for i in range(26)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a,b):
            root_a = find(a)
            root_b = find(b)
            parent[root_b] = root_a
        for equation in equations:
            if equation[1] == "!":
                continue
            a = ord(equation[0]) - ord('a')
            b = ord(equation[3]) - ord('a')
            union(a,b)
                       
        for equation in equations:
            if equation[1] != "!":
                continue
            a = ord(equation[0]) - ord('a')
            b = ord(equation[3]) - ord('a')
            if find(a) == find(b):
                return False
        return True