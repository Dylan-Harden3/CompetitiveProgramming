class Solution:
    def trap(self, height: List[int]) -> int:
        maxToLeft = []
        m = -1
        for h in height:
            maxToLeft.append(m)
            m = max(m, h)
        m = -1
        maxToRight = []
        for h in height[::-1]:
            maxToRight.append(m)
            m = max(m, h)
        maxToRight = maxToRight[::-1]

        water = 0
        for i, h in enumerate(height):
            water += max(0, min(maxToLeft[i], maxToRight[i])-h)

        return water
