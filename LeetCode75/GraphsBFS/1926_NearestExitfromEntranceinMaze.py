class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        M, N = len(maze), len(maze[0])

        queue = deque([(entrance[0], entrance[1], 0)])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visited = set()
        while queue:
            row, col, steps = queue.pop()
            if (row, col) in visited:
                continue
            visited.add((row, col))
            if [row, col] != entrance and (row == 0 or col == 0 or row == M-1 or col == N-1):
                return steps

            for dr, dc in dirs:
                if min(row + dr, col + dc) >= 0 and row + dr < M and col + dc < N \
                    and maze[row+dr][col+dc] != '+':
                    queue.appendleft((row + dr, col + dc, steps + 1))

        return -1
