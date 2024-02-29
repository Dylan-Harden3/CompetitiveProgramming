class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def dp(i):
            if i > len(cost):
                return math.inf
            
            if i in cache:
                return cache[i]

            cache[i] = min(cost[i] + dp(i+1), cost[i] + dp(i+2))
            return cache[i]

        cache[len(cost)] = 0

        dp(0)
        return min(cache[0], cache[1])
