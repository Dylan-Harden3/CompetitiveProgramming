class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        HashSet = set()
        for i in nums:
            if i in HashSet:
                return True
            else:
                HashSet.add(i)
        return False