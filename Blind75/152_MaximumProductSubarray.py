class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min, cur_max = nums[0], nums[0]
        res = nums[0]

        for num in nums[1:]:
            m = cur_max
            cur_max = max(num, num * cur_max, num * cur_min)
            cur_min = min(num * m, num * cur_min, num)
            res = max(res, cur_max)

        return res
