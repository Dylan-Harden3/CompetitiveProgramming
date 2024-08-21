class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        cache = {}        
        def dp(l, r):
            if (l, r) in cache:
                return cache[(l, r)]

            if l-r == 0:
                return 0

            left = piles[l] if (r-l) else 0
            right = piles[r] if (r-l) else 0

            cache[(l, r)] = res = max(left + dp(l+1, r), right + dp(l, r-1))
            return res
        return dp(0, len(piles)-1) > sum(piles) // 2
