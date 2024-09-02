class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = inf
        while l <= r:
            m = (l + r) // 2
            res = min(res, nums[m], nums[l], nums[r])

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

        return res
