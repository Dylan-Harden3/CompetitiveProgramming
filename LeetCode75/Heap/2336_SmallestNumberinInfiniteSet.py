class SmallestInfiniteSet:

    def __init__(self):
        self.nums = []
        self.cur = 1

    def popSmallest(self) -> int:
        if self.nums:
            return heapq.heappop(self.nums)
        self.cur += 1
        return self.cur - 1
    def addBack(self, num: int) -> None:
        self.

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
