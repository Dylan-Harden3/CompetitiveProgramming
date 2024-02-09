class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums) % 3 != 0:
            return []


        nums.sort()

        sol = []

        for i in range(0, len(nums), 3):
            n1, n2, n3 = nums[i:i+3]

            if abs(n1-n2) > k or abs(n2-n3) > k or abs(n3-n1) > k:
                return []
            sol.append(nums[i:i+3])
        return sol
