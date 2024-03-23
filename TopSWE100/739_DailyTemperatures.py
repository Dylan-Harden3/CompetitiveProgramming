class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = [] #(idx, tmp)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                oldIdx, oldTemp = stack.pop()
                res[oldIdx] = i-oldIdx
            stack.append((i, temp))
        return res
