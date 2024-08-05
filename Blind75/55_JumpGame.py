class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxPos = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= maxPos:
                maxPos = i
        return maxPos == 0