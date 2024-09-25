class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
    
        cache = {}

        def dp(i, j):
            if i == len(s1) and j == len(s2):
                return True
            elif i == len(s1):
                return s2[j:] == s3[i+j:]
            elif j == len(s2):
                return s1[i:] == s3[i+j:]
            
            if (i, j) in cache:
                return cache[(i, j)]

            res = False
            if s1[i] != s3[i+j] and s2[j] != s3[i+j]:
                return False
            elif s1[i] == s3[i+j] and s2[j] == s3[i+j]:
                res = res or dp(i+1, j) or dp(i, j+1)
            elif s1[i] == s3[i+j]:
                res = res or dp(i+1, j)
            elif s2[j] == s3[i+j]:
                res = res or dp(i, j+1)
            cache[(i, j)] = res
            return res
        
        return dp(0, 0)
