class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R, C = len(heights), len(heights[0])
        visited = set()
        e = [[inf] * C for _ in range(R)]
        q = [(0, 0, 0)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            effort, r, c = heapq.heappop(q)
            visited.add((r, c))
            if r == R-1 and c == C-1:
                return effort
            for dr, dc in dirs:
                newR, newC = r+dr, c+dc
                if min(newR, newC) < 0 or newR == R or newC == C or (newR, newC) in visited:
                    continue
                newDiff = max(effort, abs(heights[r][c] - heights[newR][newC]))
                if newDiff < e[newR][newC]:
                    e[newR][newC] = newDiff
                    heapq.heappush(q, (newDiff, newR, newC))
