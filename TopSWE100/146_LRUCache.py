class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = {} # key -> node
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.prev = self.tail
        self.tail.next = self.head

    def insert(self, key, value):
        node = Node(key, value)
        node.prev = self.head.prev
        self.head.prev.next = node
        self.head.prev = node
        node.next = self.head
        self.hm[key] = node
    
    def delete(self, key):
        if key not in self.hm:
            return
        node = self.hm[key]
        node.next.prev = node.prev
        node.prev.next = node.next
        self.hm.pop(node.key)

    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1

        val = self.hm[key].val
        self.delete(key)
        self.insert(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        self.delete(key)
        self.insert(key, value)

        if len(self.hm.keys()) > self.capacity:
            self.delete(self.tail.next.key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
