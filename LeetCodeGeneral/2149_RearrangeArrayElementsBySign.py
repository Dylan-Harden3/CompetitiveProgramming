class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []

        for n in nums:
            if n >= 0:
                positive.append(n)
            else:
                negative.append(n)

        res = []

        for i in range(len(positive)):
            res.append(positive[i])
            res.append(negative[i])

        return res
