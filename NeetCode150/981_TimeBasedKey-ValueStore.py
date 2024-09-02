class TimeMap:

    def __init__(self):
        self.sets = defaultdict(list)        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.sets[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.sets[key]
        if not arr or arr[0][1] > timestamp:
            return ""

        l, r = 0, len(arr)-1
        res = 0
        while l <= r:
            m = (l + r) // 2
            if arr[m][1] <= timestamp:
                res = max(m, res)
                l = m + 1
            else:
                r = m - 1

        return arr[res][0]
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
