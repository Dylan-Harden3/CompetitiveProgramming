class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        expected = sorted(heights)
        sol = 0
        for h, e in zip(heights, expected):
            if h != e:
                sol += 1
        return sol