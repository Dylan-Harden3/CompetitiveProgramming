class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def inBounds(r, c):
            return min(r, c) >= 0 and r < M and c < N

        region = set()
        rows = set()
        cols = set()

        def dfs(r, c):
            if (r, c) in region:
                return

            region.add((r, c))
            rows.add(r)
            cols.add(c)

            for dr, dc in dirs:
                if inBounds(r+dr, c+dc) and board[r+dr][c+dc] == "O":
                    dfs(r+dr, c+dc)
        
        def fill(region):
            for r, c in region:
                board[r][c] = "X"
        
        for i in range(M):
            for j in range(N):
                if board[i][j] == "O":
                    dfs(i, j)

                    if not(0 in rows or M-1 in rows or 0 in cols or N-1 in cols):
                        fill(region)
                    
                region.clear()
                rows.clear()
                cols.clear()
                
