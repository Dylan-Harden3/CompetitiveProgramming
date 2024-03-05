class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minSoFar = inf
        for price in prices:
            res = max(res, price - minSoFar)
            minSoFar = min(minSoFar, price)
        
        return res
