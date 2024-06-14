class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        sol = 0
        max_sf = -1
        for i in range(len(nums)):
            if nums[i] <= max_sf:
                sol += max_sf-nums[i] + 1
                nums[i] = max_sf + 1
            max_sf = max(max_sf, nums[i])
        return sol