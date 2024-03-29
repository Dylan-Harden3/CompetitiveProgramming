class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num, count = max(nums), 0
        l = 0
        res = 0

        for r in range(len(nums)):
            if nums[r] == max_num:
                count += 1
            
            while count == k:
                if nums[l] == max_num:
                    count -= 1
                l += 1
            res += l
        return res
