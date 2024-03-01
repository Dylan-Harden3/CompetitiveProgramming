class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                idx, t = stack.pop()
                answer[idx] = i - idx

            stack.append((i, temp))
        return answer
