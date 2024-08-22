class Solution:
    def numDecodings(self, s: str) -> int:

        digits= []
        for i in range(10):
            digits.append(str(i))


        cache = {}
        def dp(i):
            if i in cache:
                return cache[i]
            
            if i == len(s):
                return 1
            if i > len(s):
                return 0
            if s[i] == "0":
                return 0
            
            res = dp(i+1)
            if s[i] == "1" or (s[i] == "2" and i+1 < len(s) and int(s[i+1]) < 7):
                res += dp(i+2)
            
            cache[i] = res
            return res

        return dp(0)
