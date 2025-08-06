# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1]:
            return -1
        queue = deque([(0,0,1)])
        visited = set((0,0))
        while queue:
            
            row , col, length = queue.popleft()
            if row == n-1 and col == n-1:
                return length

            for dr,dc in directions:
                newRow, newCol = dr + row, dc + col
                if (newRow,newCol) not in visited and inbound(newRow,newCol) and grid[newRow][newCol] == 0:
                    visited.add((newRow,newCol))
                    queue.append((newRow,newCol,length + 1))
        return -1
