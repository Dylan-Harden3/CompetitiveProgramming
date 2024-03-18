class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []

        def backtrack(n, i):
            if n < 0 or i == len(candidates):
                return
            elif n == 0:
                res.append(stack.copy())
                return

            stack.append(candidates[i])
            backtrack(n-candidates[i], i)
            stack.pop()
            backtrack(n, i+1)
        
        backtrack(target, 0)
        return res
