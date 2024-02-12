class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1, p2 = 0, len(height)-1

        max_water = 0
        while p1 < p2:
            max_water = max(max_water, (p2-p1) * min(height[p2], height[p1]))

            if height[p2] < height[p1]:
                p2 -= 1
            else:
                p1 += 1
        return max_water
