class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        res = inf

        while l <= r:
            m = (l+r) // 2
            res = min(res, nums[l], nums[r], nums[m])

            if nums[r] > nums[l]:
                r = m - 1
            else: # nums[r] < nums[l]
                if nums[m] < nums[l]:
                    r = m-1
                else:
                    l = m + 1
        return res