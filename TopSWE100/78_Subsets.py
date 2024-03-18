class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []
        def backtrack(i, j): # at len i prefix we want to only add j:
            res.append(stack.copy())
            if i == len(nums):
                return

            idx = j
            for num in nums[j:]:
                stack.append(num)
                backtrack(i+1, idx+1)
                stack.pop()
                idx += 1

        backtrack(0, 0)
        return res
