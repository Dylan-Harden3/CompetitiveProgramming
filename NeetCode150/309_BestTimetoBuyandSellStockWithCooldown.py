class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dp(i, shares):
            if (i, shares) in cache:
                return cache[(i, shares)]
            
            if i >= len(prices):
                return 0

            res = dp(i+1, shares) # do nothing
            if shares == -1: # can buy
                res = max(res, dp(i+1, prices[i])) # buy
            elif shares >= 0: # can sell
                res = max(res, prices[i] - shares + dp(i+2, -1)) # sell
            
            cache[(i, shares)] = res
            return res
        return dp(0, -1)
