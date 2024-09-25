class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = {amount: 0}
        res = inf
        def dp(cur):
            if cur in cache:
                return cache[cur]
            
            if cur > amount:
                return inf
            res = inf
            for coin in coins:
                res = min(res, 1 + dp(cur + coin))
            
            cache[cur] = res
            return res
        return dp(0) if dp(0) != inf else -1
