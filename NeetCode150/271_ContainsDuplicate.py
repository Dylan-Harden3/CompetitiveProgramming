class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for k, v in Counter(nums).items():
            if v > 1:
                return True
        return False
