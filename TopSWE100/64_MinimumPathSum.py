class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                if not (i == (M-1) and j == (N-1)):
                    temp = math.inf
                    if i < M-1:
                        temp = min(grid[i][j] + grid[i+1][j], temp)
                    if j < N-1:
                        temp = min(grid[i][j] + grid[i][j+1], temp)
                    grid[i][j] = temp

        return grid[0][0]