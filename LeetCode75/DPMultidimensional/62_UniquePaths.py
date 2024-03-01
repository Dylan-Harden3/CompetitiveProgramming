class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {(m-1, n-1): 1}

        def dp(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            
            if min(i, j) < 0 or i > m-1 or j > n-1:
                return 0

            cache[(i, j)] = dp(i+1, j) + dp(i, j+1)
            return cache[(i, j)]

        return dp(0, 0)
