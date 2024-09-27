class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        cache = {}
        nums = [1] + nums + [1]
        def dp(l, r):
            if l > r:
                return 0
            
            if (l, r) in cache:
                return cache[(l, r)]
            
            cache[(l, r)] = 0
            for i in range(l, r+1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += dp(l, i-1) + dp(i+1, r)
                cache[(l, r)] = max(coins, cache[(l, r)])
            
            return cache[(l, r)]
        return dp(1, len(nums)-2)