class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]

            if i >= len(arr):
                return 0

            m = 0
            sol = 0
            for j in range(k):
                if i + j >= len(arr):
                    break

                m = max(m, arr[i+j])
                sol = max(sol, dfs(i+j+1) + (j+1) * m)
            dp[i] = sol
            return sol
        return dfs(0)
