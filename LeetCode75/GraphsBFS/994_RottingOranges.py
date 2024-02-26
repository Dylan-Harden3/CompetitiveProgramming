class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        freshOranges = 0
        queue = deque()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    freshOranges += 1
                elif grid[i][j] == 2:
                    queue.appendleft((i, j))
        
        steps = 0
        while queue and freshOranges > 0:
            rotten = len(queue)
            for _ in range(rotten):
                r, c = queue.pop()
                for dr, dc in dirs:
                    if min(r + dr, c + dc) >= 0 \
                        and r + dr < M and c + dc < N \
                        and grid[r + dr][c + dc] == 1:
                        freshOranges -= 1
                        grid[r + dr][c + dc] = 2
                        queue.appendleft((r + dr, c + dc))
            steps += 1
        
        return steps if freshOranges == 0 else -1
