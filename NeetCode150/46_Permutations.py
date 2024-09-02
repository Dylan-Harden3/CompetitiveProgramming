class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        bag = set()
        sols = []
        stack = []

        def backtrack():
            if len(stack) == len(nums):
                sols.append(stack.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in bag:
                    bag.add(nums[i])
                    stack.append(nums[i])
                    backtrack()
                    stack.pop()
                    bag.remove(nums[i])
        backtrack()
        return sols
