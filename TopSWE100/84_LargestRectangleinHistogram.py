class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                res = max(res, (i-idx)*height)
                start = idx
            stack.append((start, h))
        for i, h in stack:
            res = max(res, (len(heights)-i)*h)
        return res
