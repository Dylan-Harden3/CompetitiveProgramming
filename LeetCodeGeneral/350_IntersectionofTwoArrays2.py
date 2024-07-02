class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1, c2 = Counter(nums1), Counter(nums2)

        both = set(nums1).intersection(set(nums2))

        res = []
        for n in both:
            for _ in range(min(c1[n], c2[n])):
                res.append(n)

        return res