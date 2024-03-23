class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0

        profit = 0
        curP = prices[0]
        for price in prices:
            if price > curP:
                profit += price - curP
            curP = price
        return profit
