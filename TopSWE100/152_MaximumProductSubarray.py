class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        min_p, max_p = 1, 1

        for num in nums:
            temp = num * max_p
            max_p = max(num, temp, num * min_p)
            min_p = min(num, min_p * num, temp)
            res = max(res, max_p)
        return res