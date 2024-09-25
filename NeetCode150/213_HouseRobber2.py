class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache = {}

        def dp(i):
            if i >= len(nums):
                return 0
            elif i in cache:
                return cache[i]
            
            res = max(nums[i] + dp(i+2), dp(i+1))
            cache[i] = res
            return res
        
        cur = nums
        nums = nums[:-1]
        sol = dp(0)
        cache.clear()
        nums = cur[1:]
        return max(sol, dp(0))
