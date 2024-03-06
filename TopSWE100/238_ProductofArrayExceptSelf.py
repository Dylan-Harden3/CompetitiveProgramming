class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]

        cur = nums[-1]
        for i in range(n-2, -1, -1):
            res[i] *= cur
            cur *= nums[i]

        return res
