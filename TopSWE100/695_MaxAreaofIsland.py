class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j):
            if min(i, j) < 0 or i == ROWS or j == COLS:
                return 0

            if grid[i][j] == 1:
                grid[i][j] = 0
                res = 1
                for dr, dc in dirs:
                    res += dfs(i+dr, j+dc)
                return res
            else:
                return 0
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res
