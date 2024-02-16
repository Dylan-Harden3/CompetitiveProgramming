class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        res = 0
        for i in range(len(self.requests)-1, -1, -1):
            if self.requests[i] >= t - 3000:
                res += 1
            else:
                break
        return res

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
