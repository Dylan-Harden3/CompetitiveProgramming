class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = -1
        res = 1
        cur = 0
        for r in range(len(nums)):
            while cur & nums[r]:
                l += 1
                cur = cur ^ nums[l]
            cur = cur | nums[r]
            res = max(res, r-l)
        return res