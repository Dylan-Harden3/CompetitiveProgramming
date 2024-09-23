class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        res, cur = 0, 0
        def dfs(i, j):
            if min(i, j) < 0 or i == M or j == N or grid[i][j] == 0:
                return
            grid[i][j] = 0
            nonlocal cur
            cur += 1
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    cur = 0
                    dfs(i, j)
                    res = max(res, cur)
        
        return res
