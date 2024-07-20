class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        pacific = set()
        atlantic = set()
        ROWS, COLS = len(heights), len(heights[0])

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, sols, prev_height):
            if (r, c) in sols or min(r, c) < 0  or r == ROWS or c == COLS or heights[r][c] < prev_height:
                return

            sols.add((r, c))
            
            for dr, dc in dirs:
                newr, newc = r+dr, c+dc
                dfs(newr, newc, sols, heights[r][c])
        
        for i in range(COLS):
            dfs(0, i, pacific, -1)
            dfs(ROWS-1, i, atlantic, -1)
        
        for i in range(ROWS):
            dfs(i, 0, pacific, -1)
            dfs(i, COLS-1, atlantic, -1)
        
        res = []
        for r, c in atlantic:
            if (r, c) in pacific:
                res.append([r, c])
        return res