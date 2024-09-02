class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sols = []
        stack = []
        res = set()
        def backtrack(i, skip):
            if i == len(nums):
                if str(stack) not in res:
                    sols.append(stack.copy())
                    res.add(str(stack))
                return
            
            if not skip:
                stack.append(nums[i])

            for j in range(i+1, len(nums)+1):
                backtrack(j, True)
                backtrack(j, False)
            
            if not skip:
                stack.pop()

        backtrack(0, False)
        backtrack(0, True)
        return sols
