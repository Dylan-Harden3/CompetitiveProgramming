class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        cache = {}
        visit = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dp(i, j):
            if min(i, j) < 0 or i == M or j == N:
                return -inf
            if (i, j) in cache:
                return cache[(i, j)]
            
            lis = 1
            visit.add((i, j))
            for di, dj in dirs:
                r, c = i+di, j+dj
                if not(min(r, c) < 0 or r == M or c == N) and matrix[r][c] > matrix[i][j] and (r, c) not in visit:
                    lis = max(lis, 1 + dp(r, c))
            visit.remove((i, j))
            cache[(i, j)] = lis
            return lis
        res = 1
        for i in range(M):
            for j in range(N):
                res = max(res, dp(i, j))
        return res
