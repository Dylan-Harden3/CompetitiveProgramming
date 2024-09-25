class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = 0
        cache = {}

        def dp(i, cur):
            if (i, cur) in cache:
                return cache[(i, cur)]
            if cur == amount:
                return 1
            elif cur > amount or i == len(coins):
                return 0
            res = dp(i+1, cur) + dp(i, cur + coins[i])

            cache[(i, cur)] = res
            return res

        return dp(0, 0)
