class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        q = deque([])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    q.append((i, j, 0))

        def inBounds(i, j):
            return not(min(i, j) < 0 or i == M or j == N or grid[i][j] != 1)
        
        res = 0
        while q:
            i, j, t = q.pop()
            if grid[i][j] != 2:
                res = max(res, t)
            grid[i][j] = 2

            for di, dj in dirs:
                if inBounds(i+di, j+dj):
                    q.appendleft((i+di, j+dj, t+1))

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    return -1
        return res
