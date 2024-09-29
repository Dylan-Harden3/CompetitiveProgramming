class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        original = 0

        for i, n in enumerate(digits[::-1]):
            original += (10**i) * n
        original += 1
        res = []
        while original:
            res.append(original % 10)
            original = original // 10
        return res[::-1]
