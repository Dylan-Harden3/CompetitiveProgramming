class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = {n: 0}

        def backtrack(i):
            if i in dp:
                return dp[i]
            if i > n:
                return inf
            res = cost[i] + min(backtrack(i+1), backtrack(i+2))
            dp[i] = res
            return res
        
        return min(backtrack(0), backtrack(1))
