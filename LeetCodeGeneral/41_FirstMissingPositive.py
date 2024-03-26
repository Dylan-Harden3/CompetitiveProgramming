class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if n < 0:
                nums[i] = 0

        for i, n in enumerate(nums):
            idx = abs(n)-1

            if idx >= 0 and idx < len(nums):
                if nums[idx] > 0:
                    nums[idx] = -nums[idx]
                elif nums[idx] == 0:
                    nums[idx] = -len(nums)

        for i in range(len(nums)):
            if nums[i] >= 0:
                return i+1

        return len(nums)+1

