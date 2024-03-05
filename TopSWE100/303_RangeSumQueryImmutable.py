class NumArray:

    def __init__(self, nums: List[int]):
        self.pf = [0]
        for num in nums:
            self.pf.append(num + self.pf[-1])
        print(self.pf)

    def sumRange(self, left: int, right: int) -> int:
        return self.pf[right+1] - self.pf[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
