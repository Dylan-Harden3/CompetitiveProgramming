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
        if head is None: return None
        node_map = {}

        cur = head
        while cur:
            node_map[cur] = ListNode(cur.val)
            cur = cur.next

        node_map[None] = None
        
        cur = head
        while cur:
            node_map[cur].next = node_map[cur.next]
            node_map[cur].random = node_map[cur.random]
            cur = cur.next
        return node_map[head]
