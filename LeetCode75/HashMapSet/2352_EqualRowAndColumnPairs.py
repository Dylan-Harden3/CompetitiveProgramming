class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        N = len(grid)
        rows = defaultdict(int)
        cols = defaultdict(int)

        for row in grid:
            rows[tuple(row)] += 1

        for i in range(N):
            curCol = []
            for j in range(N):
                curCol.append(grid[j][i])

            cols[tuple(curCol)] += 1

        res = 0
        used = set()
        for row in grid:
            if tuple(row) not in used:
                res += rows[tuple(row)] * cols[tuple(row)]
                used.add(tuple(row))

        return res
