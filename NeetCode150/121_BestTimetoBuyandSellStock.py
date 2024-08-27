class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minsofar = prices[0]

        for p in prices[1:]:
            res = max(res, p-minsofar)
            minsofar = min(minsofar, p)
        
        return res
