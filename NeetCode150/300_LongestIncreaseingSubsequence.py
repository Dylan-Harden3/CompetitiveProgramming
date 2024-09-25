class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {len(nums): 0}

        def dp(i):
            if i in cache:
                return cache[i]
            res = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    res = max(res, 1 + dp(j))
            cache[i] = res
            return res
        
        return max([dp(i) for i in range(len(nums))])
