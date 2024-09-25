class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        cache = {(-1, -1): 0}
        for i in range(len(word1)):
            cache[(i, -1)] = i+1
        for j in range(len(word2)):
            cache[(-1, j)] = j+1
        def dp(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            res = 1 + min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1))
            if word1[i] == word2[j]:
                res = min(res, dp(i-1, j-1))
            cache[(i, j)] = res
            return res
        
        dp(len(word1)-1, len(word2)-1)
        print(cache)
        return dp(len(word1)-1, len(word2)-1)
        
