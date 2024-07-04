class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        msf = inf
        mp = 0
        for p in prices:
            msf = min(msf, p)

            mp = max(mp, p - msf)
        return mp