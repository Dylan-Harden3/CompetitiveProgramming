class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        most_candies = max(candies)
        res = [False] * len(candies)
        for i,c in enumerate(candies):
            if c + extraCandies >= most_candies:
                res[i] = True
        return res
