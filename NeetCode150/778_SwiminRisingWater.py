class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        heap = [(grid[0][0], 0, 0)]
        while heap:
            cost, i, j = heapq.heappop(heap)
            if (i, j) in visit:
                continue
            
            visit.add((i, j))
            if i == N-1 and j == N-1:
                return cost
            for di, dj in dirs:
                r, c = i+di, j+dj
                if min(r, c) >= 0 and max(r, c) < N and (r, c) not in visit:
                    heapq.heappush(heap, (max(cost, grid[r][c]), r, c))
        


