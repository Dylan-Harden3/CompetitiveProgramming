class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        candidate = nums[0]
        for n in nums[1:]:
            candidate = candidate ^ n
        return candidate
