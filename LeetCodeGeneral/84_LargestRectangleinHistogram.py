class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(heights):
            idx = i
            while stack and stack[-1][1] > h:
                idx, oldH = stack.pop()
                res = max(res, oldH * (i-idx))
            stack.append((idx, h))

        for i, h in stack:
            res = max(res, h * (len(heights) - i))
        
        return res
