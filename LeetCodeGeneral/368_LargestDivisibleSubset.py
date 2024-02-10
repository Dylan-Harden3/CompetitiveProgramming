class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        nums.sort()

        dp = [1] * len(nums)
        ms, midx = 1, 0

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] > ms:
                        ms = dp[i]
                        midx = i
        
        res = []
        num = nums[midx]
        for i in range(midx, -1, -1):
            if num % nums[i] == 0 and dp[i] == ms:
                res.append(nums[i])
                num = nums[i]
                ms -= 1
        return res
