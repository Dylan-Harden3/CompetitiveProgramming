class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        negative = [n**2 for n in nums if n < 0][::-1]
        positive = [n**2 for n in nums if n >= 0]

        n, p = 0, 0

        res = []
        while n < len(negative) and p < len(positive):
            if negative[n] < positive[p]:
                res.append(negative[n])
                n += 1
            else:
                res.append(positive[p])
                p += 1
        
        while n < len(negative):
            res.append(negative[n])
            n += 1

        while p < len(positive):
            res.append(positive[p])
            p += 1

        return res
