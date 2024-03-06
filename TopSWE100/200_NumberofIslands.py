class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j):
            if min(i, j) < 0 or i == ROWS or j == COLS:
                return

            if grid[i][j] == '1':
                grid[i][j] = '0'

                for dr, dc in dirs:
                    dfs(i+dr, j+dc)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)

        return res
