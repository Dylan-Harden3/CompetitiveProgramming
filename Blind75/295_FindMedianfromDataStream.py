class MedianFinder:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def addNum(self, num: int) -> None:
        if not self.q1 or num <= -self.q1[0]:
            heappush(self.q1, -num)
        else:
            heappush(self.q2, num)

        if len(self.q1) > len(self.q2)+1:
            el = -heappop(self.q1)
            heappush(self.q2, el)
        if len(self.q2) > len(self.q1)+1:
            el = -heappop(self.q2)
            heappush(self.q1, el)

    def findMedian(self) -> float:
        if (len(self.q1) + len(self.q2)) % 2:
            return -self.q1[0] if len(self.q1) > len(self.q2) else self.q2[0]
        
        return (-self.q1[0] + self.q2[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()