"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        cur = head
        m = {}
        while cur:
            m[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur.next:
            m[cur].next = m[cur.next]
            cur = cur.next
        
        cur = head
        while cur:
            if cur.random:
                m[cur].random = m[cur.random]
            cur = cur.next

        return m[head]