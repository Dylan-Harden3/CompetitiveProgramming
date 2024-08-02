class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        cache[0] = 0
        def dp(amount):
            if amount in cache:
                return cache[amount]
            if amount < 0:
                return inf
            
            res = inf
            for coin in coins:
                res = min(res, dp(amount - coin)+1)
            
            cache[amount] = res
            return res
        dp(amount)
        return cache[amount] if cache[amount] is not inf else -1