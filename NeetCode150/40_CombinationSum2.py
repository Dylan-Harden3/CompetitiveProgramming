class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []
        candidates.sort()
        nums = candidates

        def backtrack(i, total):
            if total == target:
                res.append(stack.copy())
                return
                
            if total > target or i == len(nums):
                return

            stack.append(nums[i])
            backtrack(i+1, total + nums[i])
            stack.pop()

            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            
            backtrack(i+1, total)
        backtrack(0, 0)
        return res
