class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        self.inc = defaultdict(int)

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append((x, len(self.stack)+1))

    def pop(self) -> int:
        if not self.stack:
            return -1
        el, n = self.stack.pop()
        add = self.inc[n]
        self.inc.pop(n)
        return el + add

    def increment(self, k: int, val: int) -> None:
        for i in range(k, 0, -1):
            if i <= len(self.stack):
                self.inc[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
