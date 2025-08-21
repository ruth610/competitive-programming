# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parent = list(range(n))
        # print(parent)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parent[root_y] = root_x
        edgeList.sort(key=lambda x:x[2])        
        q = [(l,u,v,i) for i,(u,v,l) in enumerate(queries)]
        q.sort()
        size = len(queries)
        ans = [False] * size
        edge_size = len(edgeList)
        edge_index = 0
        for q_limit,u,v,i in q:
            while edge_index < edge_size and edgeList[edge_index][2]  < q_limit:
                union(edgeList[edge_index][0],edgeList[edge_index][1])   
                edge_index += 1
            ans[i] = find(u) == find(v)
        return ans
        