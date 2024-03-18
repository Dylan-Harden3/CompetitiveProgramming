class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        bag = set()
        stack = []

        def backtrack():
            if len(stack) == len(nums):
                res.append(stack.copy())
                return
            
            for i in range(len(nums)):
                if i not in bag:
                    bag.add(i)
                    stack.append(nums[i])
                    backtrack()
                    bag.remove(i)
                    stack.pop()
        backtrack()
        return res
