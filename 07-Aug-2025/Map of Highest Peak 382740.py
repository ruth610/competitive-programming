# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        def inbound(row,col):
            return  0 <= row < len(isWater) and 0 <= col < len(isWater[0])
        result = [[-1 for _ in range(len(isWater[0]))] for _ in range(len(isWater)) ]
        queue = deque()
        visited = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        for row in range(len(isWater)):
            for col in range(len(isWater[0])):
                if isWater[row][col] == 1:
                    isWater[row][col] = 0
                    queue.append((row,col))
                    visited.add((row,col))

        while queue:
            row,col = queue.popleft()
            for dr,dc in directions:
                newRow, newCol = dr + row, dc + col
                if inbound(newRow,newCol) and isWater[newRow][newCol] == 0 and (newRow,newCol) not in visited:
                    isWater[newRow][newCol] = isWater[row][col] + 1
                    queue.append((newRow,newCol))
                    visited.add((newRow,newCol))
        return isWater
                

        