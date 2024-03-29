class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        cur = deque()
        while len(self.q) > 1:
            cur.append(self.q.popleft())
        res = self.q[0]
        self.q = cur
        return res

    def top(self) -> int:
        cur = deque()
        while len(self.q) > 1:
            cur.append(self.q.popleft())
        res = self.q[0]
        cur.append(self.q.popleft())
        self.q = cur
        return res

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
