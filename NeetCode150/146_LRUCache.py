class ListNode:
    def __init__(self):
        self.next = None
        self.prev = None
        self.val = None
        self.key = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.head = ListNode()
        self.tail = ListNode()

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        
        node = self.nodes[key]

        # remove
        if self.nodes[key].prev:
            self.nodes[key].prev.next = self.nodes[key].next
        if self.nodes[key].next:
            self.nodes[key].next.prev = self.nodes[key].prev

        # add to front
        old_start = self.head.next
        old_start.prev = self.nodes[key]
        self.nodes[key].next = old_start
        self.nodes[key].prev = self.head
        self.head.next = self.nodes[key]

        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.nodes:
            self.nodes[key] = ListNode()
        self.nodes[key].key = key
        self.nodes[key].val = value

        if len(self.nodes) == 1:
            self.head.next = self.nodes[key]
            self.tail.prev = self.nodes[key]
            self.nodes[key].next = self.tail
            self.nodes[key].prev = self.head
        else:
            # remove key from list:
            if self.nodes[key].prev:
                self.nodes[key].prev.next = self.nodes[key].next
            if self.nodes[key].next:
                self.nodes[key].next.prev = self.nodes[key].prev

            # add it to the front
            old_start = self.head.next
            old_start.prev = self.nodes[key]
            self.nodes[key].next = old_start
            self.nodes[key].prev = self.head
            self.head.next = self.nodes[key]

            # evict
            if len(self.nodes) > self.capacity:
                key_to_evict = self.tail.prev.key
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev

                self.nodes.pop(key_to_evict)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
