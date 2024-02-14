class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1 = set(nums1)
        n2 = set(nums2)

        return [n1 - n1.intersection(n2), n2 - n2.intersection(n1)]




