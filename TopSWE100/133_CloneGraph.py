"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def helper(node):
            if not node: return None
            if node in visited: return visited[node]
            
            head = Node(node.val)
            visited[node] = head
            for nei in node.neighbors:
                if nei not in visited:
                    helper(nei)
                head.neighbors.append(visited[nei])
            return head
        return helper(node)