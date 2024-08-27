class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEatAll(k):
            t = 0
            for pile in piles:
                t += ceil(pile / k) if k > 0 else inf
            return t <= h

        l, r = 0, max(piles)
        res = inf
        while l <= r:
            m = (l + r) // 2
            if canEatAll(m):
                r = m-1
                res = m
            else:
                l = m+1
            print(l, r)

        return res
