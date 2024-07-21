class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {n: 1}

        def dp(i):
            if i in cache:
                return cache[i]
            
            if i > n:
                return 0
            
            res = dp(i+1) + dp(i+2)
            cache[i] = res
            return res
        
        dp(0)
        return cache[0]