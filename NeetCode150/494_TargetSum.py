class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = {}
        def dp(i, amount):
            if i == len(nums):
                if amount == target:
                    return 1
                else:
                    return 0
            if (i, amount) in cache:
                return cache[(i, amount)]
            
            res = dp(i+1, amount - nums[i]) + dp(i+1, amount + nums[i])
            cache[(i, amount)] = res
            return res

        return dp(0, 0)
