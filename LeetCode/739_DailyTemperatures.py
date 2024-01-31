class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack:
                top = temperatures[stack[-1]]
                if top < temp:
                    sol[stack[-1]] = idx - stack[-1]
                    stack.pop()
                else:
                    break
            stack.append(idx)
        return sol
