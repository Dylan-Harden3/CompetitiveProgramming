class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid1), len(grid1[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j):
            res = True
            if 0 <= i < ROWS and 0 <= j < COLS and grid2[i][j] == 1:
                if grid1[i][j] != 1: return False
                grid2[i][j] = -1
                for dr, dc in dirs:
                    res &= dfs(i+dr, j+dc)
            return res

    
        for i in range(ROWS):
            for j in range(COLS):
                if grid2[i][j] == 1:
                    res += dfs(i, j)
        return res
