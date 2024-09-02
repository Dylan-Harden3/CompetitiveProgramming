class MedianFinder:

    def __init__(self):
        self.h1 = []
        self.h2 = []

    def addNum(self, num: int) -> None:
        if self.h2 and num >= self.h2[0]:
            heappush(self.h2, num)
        else:
            heappush(self.h1, -num)

        if len(self.h2) > len(self.h1)+1:
            heappush(self.h1, -heappop(self.h2))
        elif len(self.h1) > len(self.h2)+1:
            heappush(self.h2, -heappop(self.h1))

    def findMedian(self) -> float:
        is_odd = (len(self.h1) + len(self.h2)) % 2

        if is_odd:
            if len(self.h2) > len(self.h1):
                return self.h2[0]
            else:
                res = -heappop(self.h1)
                heappush(self.h1, -res)
                return res
        else:
            cur = -heappop(self.h1)
            res = (cur + self.h2[0]) / 2
            heappush(self.h1, -cur)
            return res


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
