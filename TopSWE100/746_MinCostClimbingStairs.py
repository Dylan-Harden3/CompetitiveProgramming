class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        second, first = 0, 0

        for i in range(len(cost)-1, -1, -1):
            x = min(cost[i] + first, cost[i] + second)
            second = first
            first = x
        
        return min(first, second)
