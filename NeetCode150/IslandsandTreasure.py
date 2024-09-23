from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        M, N = len(grid), len(grid[0])
        INF = 2147483647

        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def inBounds(i, j):
            return not (min(i, j) < 0 or i == M or j == N or grid[i][j] == -1)
        
        def bfs(i, j):
            q = deque([(i, j, 0)])
            visit = set()
            
            while q:
                r, c, d = q.pop()
                if grid[r][c] == 0:
                    return d
                visit.add((r, c))
                for dr, dc in dirs:
                    if (r+dr, c+dc) not in visit and inBounds(r+dr, c+dc):
                        q.appendleft((r+dr, c+dc, d+1))
            return INF
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == INF:
                    grid[i][j] = bfs(i, j)
