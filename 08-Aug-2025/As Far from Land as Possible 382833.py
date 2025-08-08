# Problem: As Far from Land as Possible - https://leetcode.com/problems/as-far-from-land-as-possible/description/

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        queue = deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    
        # print(grid)
        n = len(grid)
        if len(queue) == 0 or len(queue) == n * n:
            return -1
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        max_dist = - 1
        while queue:
            row , col = queue.popleft()
            for dr,dc in directions:
                newRow , newCol = dr + row, dc + col
                if inbound(newRow,newCol) and grid[newRow][newCol] == 0:
                    grid[newRow][newCol] = grid[row][col] + 1
                    max_dist = max(max_dist,grid[newRow][newCol])
                    queue.append((newRow,newCol))
        # print(grid)
        return max_dist - 1
                    




