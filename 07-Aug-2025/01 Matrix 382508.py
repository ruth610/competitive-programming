# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def inbound(row,col):
            return 0 <= row < len(mat) and 0 <= col < len(mat[0]) 
        queue = deque()
        result = [[-1 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    result[r][c] = 0
                    queue.append((r, c))
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        while queue:
            row, col = queue.popleft()
            
            for dr,dc in directions:
                newRow, newCol = dr + row, dc + col 
                if inbound(newRow,newCol) and result[newRow][newCol] == -1:
                    queue.append((newRow,newCol))
                    result[newRow][newCol] = result[row][col] + 1
        return result
                    
