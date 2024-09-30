class Solution:
    def trap(self, height: List[int]) -> int:
        maxToLeft = [height[0]]
        for i in range(1, len(height)):
            maxToLeft.append(max(maxToLeft[-1], height[i]))
        
        maxToRight = [height[-1]]
        for i in range(len(height)-2, -1, -1):
            maxToRight.append(max(maxToRight[-1], height[i]))
        
        maxToRight = maxToRight[::-1]

        res = 0
        for i in range(len(height)):
            res += min(maxToLeft[i], maxToRight[i]) - height[i]
        return res
