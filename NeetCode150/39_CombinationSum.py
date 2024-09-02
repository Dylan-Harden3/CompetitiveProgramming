class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sols = []
        stack = []
        def backtrack(i, total):
            if total > target or i == len(candidates):
                return

            if total == target:
                sols.append(stack.copy())
                return
            
            for j in range(i, len(candidates)):
                stack.append(candidates[j])
                backtrack(j, total + candidates[j])
                stack.pop()

        backtrack(0, 0)

        return sols
