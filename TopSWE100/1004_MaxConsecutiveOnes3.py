class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        flipped, res, l = 0, 0, 0, 
        for r in range(len(nums)):
            if not nums[r]:
                if flipped < k:
                    flipped += 1
                else:
                    while l < r and nums[l] == 1:
                        l += 1
                    l += 1
            res = max(res, r-l+1)
        return res