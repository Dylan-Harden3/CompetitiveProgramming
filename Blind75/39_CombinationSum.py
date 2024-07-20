class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sols = []
        comb = []
        def helper(cur_sum, index):
            if index == len(candidates) or cur_sum > target:
                return

            if cur_sum == target:
                sols.append(comb.copy())
                return
            
            comb.append(candidates[index])
            helper(cur_sum + candidates[index], index)
            comb.pop()
            helper(cur_sum, index + 1)
        
        helper(0, 0)
        return sols