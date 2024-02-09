class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0]
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] * nums[i])

        postfix = [nums[-1]]
        for i in range(len(nums)-2, -1, -1):
            postfix.append(postfix[-1] * nums[i])

        postfix = postfix[::-1]

        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(postfix[1])
            elif i == len(nums)-1:
                res.append(prefix[-2])
            else:
                res.append(prefix[i-1] * postfix[i+1])
        return res
