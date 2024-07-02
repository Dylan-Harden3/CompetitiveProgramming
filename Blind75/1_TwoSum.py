class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bag = defaultdict(int)
        for i, n in enumerate(nums):
            if target - n in bag:
                return [bag[target - n], i]
            bag[n] = i
        
