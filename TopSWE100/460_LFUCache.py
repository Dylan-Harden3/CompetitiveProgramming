class ListNode:
    def __init__(self, val=None, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.val = val

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1, prev=self.head)
        self.head.next = self.tail
        self.nodemap = {}
    
    def length(self):
        return len(self.nodemap)
    
    def push(self, val):
        node = ListNode(val=val)
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node
        self.nodemap[val] = node
    
    def pop(self, val):
        if val in self.nodemap:
            node = self.nodemap[val]
            node.next.prev = node.prev
            node.prev.next = node.next
            self.nodemap.pop(val)
    
    def popLast(self):
        res = self.tail.prev.val
        self.pop(self.tail.prev.val)
        return res

    def update(self, val):
        self.pop(val)
        self.push(val)

class LFUCache:

    def __init__(self, capacity: int):
        self.nodeVals = {}
        self.listMap = defaultdict(LinkedList)
        self.freqMap = defaultdict(int)
        self.minFreq = 0
        self.capacity = capacity # max capacity

    def counter(self, key):
        freq = self.freqMap[key]
        self.freqMap[key] += 1
        self.listMap[freq].pop(key)
        self.listMap[freq+1].push(key)

        if freq == self.minFreq and self.listMap[freq].length() == 0:
            self.minFreq += 1
    
    def get(self, key: int) -> int:
        if key not in self.nodeVals:
            return -1
        
        self.counter(key)
        return self.nodeVals[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key not in self.nodeVals and len(self.nodeVals) == self.capacity:
            res = self.listMap[self.minFreq].popLast()
            self.nodeVals.pop(res)
            self.freqMap.pop(res)
        
        self.nodeVals[key] = value
        self.counter(key)
        self.minFreq = min(self.minFreq, self.freqMap[key])

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
