class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        def dp(i):
            if i in cache:
                return cache[i]

            if i >= len(s):
                return True

            res = False
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict:
                    res = res or dp(j)
            cache[i] = res
            return res

        return dp(0)
