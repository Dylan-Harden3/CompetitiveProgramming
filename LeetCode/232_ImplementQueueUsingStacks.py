class MyQueue:

    def __init__(self):
        self.stack = collections.deque()

    def push(self, x: int) -> None:
        self.stack.appendleft(x)

    def pop(self) -> int:
        for i in range(len(self.stack)-1):
            self.stack.append(self.stack.popleft())
        return self.stack.popleft()

    def peek(self) -> int:
        for i in range(len(self.stack)-1):
            self.stack.append(self.stack.popleft())
        res = self.stack[0]
        self.stack.append(self.stack.popleft())
        return res

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
