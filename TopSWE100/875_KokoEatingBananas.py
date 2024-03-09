class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles)

        def canEat(k):
            t = 0
            for pile in piles:
                t += ceil(pile / k) if k > 0 else math.inf
            return t <= h

        res = r
        while l <= r:
            m = (l+r)//2
            if canEat(m):
                res = m
                r = m-1
            else:
                l = m +1
        return res


