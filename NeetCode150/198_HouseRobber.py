class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = {}
        def dp(i):
            if i in cache:
                return cache[i]
            if i >= len(nums):
                return 0
            res = max(nums[i] + dp(i+2), dp(i+1))
            cache[i] = res
            return res
        return dp(0)
