class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}

        def dp(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            
            if min(i, j) < 0:
                return 0
            
            res = 0
            res = max(dp(i-1, j), dp(i, j-1))

            if text1[i] == text2[j]:
                res = max(res, 1 + dp(i-1, j-1))

            cache[(i, j)] = res
            return res
        
        return dp(len(text1)-1, len(text2)-1)
