class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i, n in enumerate(nums):
            if i == 0:
                res.append(0)
            elif i == 1:
                res.append(nums[i-1])
            else:
                res.append(res[-1]*nums[i-1])
        cur = nums[-1]
        for i in range(len(nums)-2, 0, -1):
            res[i] *= cur
            cur *= nums[i]
        res[0] = cur
        return res
