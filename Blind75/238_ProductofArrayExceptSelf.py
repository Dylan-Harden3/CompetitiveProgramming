class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * len(nums)

        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]

        cur = nums[-1]
        for i in range(n-2, 0, -1):
            res[i] = cur * res[i]
            cur *= nums[i]
        res[0] = cur
        return res