class Solution:
    def numSquares(self, n: int) -> int:
        dp = {0: 0}

        def backtrack(num):
            if num in dp:
                return dp[num]

            if num < 0:
                return math.inf

            i = 1
            res = math.inf
            while i**2 <= num:
                res = min(res, 1 + backtrack(num - i**2))
                i += 1
            dp[num] = res
            return res
        
        return backtrack(n)
