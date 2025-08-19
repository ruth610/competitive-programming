# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class UnionFind:
    def __init__(self,n):
        self.parent = [-1 for _ in range(n )]
    def find(self,x):
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if root_x > root_y:
            root_x, root_y = root_y, root_x
        
        self.parent[root_x] += self.parent[root_y]
        self.parent[root_y] =  root_x
        return True

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        OFFSET = 10001  
        uf = UnionFind(20005) 

        for x, y in stones:
            uf.union(x, y + OFFSET)

        seen = set()
        for x, y in stones:
            seen.add(uf.find(x))

        return len(stones) - len(seen)
        # print(uf.parent)


                        

        