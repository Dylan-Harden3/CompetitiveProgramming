class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []
        sols = set()
        nums.sort()

        def backtrack(i, skip):
            if i == len(nums):
                if str(stack) not in sols:
                    sols.add(str(stack))
                    res.append(stack.copy())
                return
            if not skip:
                stack.append(nums[i])

            for j in range(i+1, len(nums)+1):
                backtrack(j, False)
                backtrack(j, True)

            if not skip:
                stack.pop()
        backtrack(0, False)
        backtrack(0, True)
        return res
