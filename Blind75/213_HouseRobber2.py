class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        cache = {}

        def dp(i):
            if i in cache:
                return cache[i]

            if i >= len(nums):
                return 0
            
            res = max(nums[i] + dp(i+2), dp(i+1))
            cache[i] = res
            return res
        cache[len(nums)-1] = 0
        res = dp(0)
        cache = {}
        res = max(res, dp(1))

        return res