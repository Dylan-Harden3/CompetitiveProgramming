class RandomizedSet:

    def __init__(self):
        self.arr= []
        self.items = {}

    def insert(self, val: int) -> bool:
        if val in self.items:
            return False
        self.arr.append(val)
        self.items[val] = len(self.arr)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.items:
            return False
        self.arr[self.items[val]] = self.arr[-1]
        self.items[self.arr[-1]] = self.items[val]
        self.arr.pop()
        self.items.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
