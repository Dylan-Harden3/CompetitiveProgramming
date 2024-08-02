class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total = sum(nums)
        cur = sum(nums[:total])
        res = total - cur
        for i in range(1, len(nums)):
            cur -= nums[i-1]
            cur += nums[total+i-1] if total + i-1 < len(nums) else nums[total + i-1 - len(nums)]
            res = min(res, total - cur)
        
        return res