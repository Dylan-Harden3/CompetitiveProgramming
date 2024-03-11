class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        curOdd = 0
        res = 0
        count = 0

        for r in range(len(nums)):
            if nums[r] % 2:
                curOdd += 1
                count = 0
            
            if curOdd == k:
                while l < r and nums[l] % 2 == 0:
                    l += 1
                    count += 1
                l += 1
                count += 1
                curOdd -=1
            res += count
        return res