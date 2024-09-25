class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        goal = sum(nums) / 2
        cache = {}
        def dp(i, amount):
            if (i, amount) in cache:
                return cache[(i, amount)]
            if i == len(nums):
                return False
            if amount == goal:
                return True
            cache[(i, amount)] = dp(i+1, amount) or dp(i+1, amount + nums[i])
            return cache[(i, amount)]
        return dp(0, 0)
