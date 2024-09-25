class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def dp(i, j):
            if j == len(t):
                return 1
            
            if i == len(s):
                return 0
            
            if (i, j) in cache:
                return cache[(i, j)]
            res = dp(i+1, j)
            if s[i] == t[j]:
                res += dp(i+1, j+1)
            cache[(i, j)] = res
            return res
        return dp(0, 0)
