# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def inbound(row,col):
            return 0 <= row < len(maze) and 0 <= col < len(maze[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        r,l = entrance
        queue = deque([(r,l,0)])
        visited = set()
        visited.add((r,l))
        while queue:
            row , col, length = queue.popleft()
            if ( row == 0 or row == len(maze) -1 or col == 0 or col == len(maze[row]) - 1) and [row,col] != entrance:
                return length
            # print(length)
            for dr, dc in directions:
                nr , nc = dr + row , dc + col
                if inbound(nr,nc) and maze[nr][nc] == "." and (nr,nc) not in visited:
                    queue.append((nr,nc,length + 1))
                    visited.add((nr,nc))
        return -1
