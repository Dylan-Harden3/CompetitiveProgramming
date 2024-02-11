class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        dp = [[0] * COLS for _ in range(COLS)]
        for r in reversed(range(ROWS)):
            cur_dp = [[0] * COLS for _ in range(COLS)]

            for c1 in range(COLS):
                for c2 in range(COLS):
                    if c1 != c2:
                        cherries = grid[r][c1] + grid[r][c2]
                        max_cherries = 0
                        for d_c1 in [-1, 0, 1]:
                            for d_c2 in [-1, 0, 1]:
                                nc1, nc2 = c1 + d_c1, c2 + d_c2
                                if min(nc1, nc2) < 0 or max(nc1, nc2) >= COLS:
                                    continue
                                max_cherries = max(
                                    max_cherries,
                                    cherries + dp[nc1][nc2]
                                )
                        cur_dp[c1][c2] = max_cherries
            dp = cur_dp
        return dp[0][COLS-1]

