class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dp(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            cache[(i, j)] = False
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if j+1 < len(p) and p[j+1] == '*':
                cache[(i, j)] = dp(i, j+2) or (match and dp(i+1, j))
                return cache[(i, j)]
            
            if match:
                cache[(i, j)] = dp(i+1, j+1)
                    
            return cache[(i, j)]
        return dp(0, 0)