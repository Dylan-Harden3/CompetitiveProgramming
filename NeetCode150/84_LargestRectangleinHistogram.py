class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        res = 0
        stack = []
        for i in range(len(heights)):
            idx = i
            while stack and stack[-1][0] > heights[i]:
                h, idx = stack.pop()
                res = max(res, h * (i-idx))
            stack.append((heights[i], idx))
        
        for h, i in stack:
            res = max(res, h * (len(heights)-i)) 
        return res
