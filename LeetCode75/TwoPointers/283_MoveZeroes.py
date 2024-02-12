class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = 0
        while p1 < len(nums) and p2 < len(nums):
            while p2 < len(nums) and nums[p2]==0:
                p2 += 1
            if p2 < len(nums):
                nums[p1] = nums[p2]
                p1 += 1
            p2 += 1

        while p1 < len(nums):
            nums[p1] = 0
            p1 += 1
