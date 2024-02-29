class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        stack = []
        def backtrack(i):
            if len(stack) > k:
                return
            
            if len(stack) == k and stack[-1][1] == n:
                res.append([s[0] for s in stack])
                return

            for j in range(i, 10):
                stack.append((j, stack[-1][1] + j) if stack else (j, j))
                backtrack(j+1)
                stack.pop()
        backtrack(1)
        return res
