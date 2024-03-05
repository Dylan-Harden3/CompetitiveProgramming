class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rems = {}

        for i, num in enumerate(nums):
            if target - num in rems:
                return [rems[target-num], i]
            
            rems[num] = i
