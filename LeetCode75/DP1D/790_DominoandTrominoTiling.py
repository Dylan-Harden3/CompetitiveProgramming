class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1: return 1
        MOD = 10**9+7
        # dp ways to fill 2*i+1
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        # dpa ways to fill 2*i with 1 filled
        dpa = [0] * n
        dpa[0] = 0
        dpa[1] = 1

        for i in range(2, n):
            dp[i] = (dp[i-2] + dp[i-1] + dpa[i-1]*2) % MOD
            dpa[i] = (dpa[i-1] + dp[i-2]) % MOD

        return dp[n-1]
