class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {n: 1}
        def search(i):
            if i in dp:
                return dp[i]
            res = search(i+1)
            if i+2 <= n:
                res += search(i+2)
            dp[i] = res
            return res
        return search(0)

