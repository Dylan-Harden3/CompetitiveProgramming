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
        if not node: return None
        node_map = {}
        visit = set()
        def dfs(node):
            if node.val not in node_map:
                node_map[node.val] = Node(val=node.val)
            visit.add(node)
            for nei in node.neighbors:
                if nei not in visit:
                    dfs(nei)
                node_map[node.val].neighbors.append(node_map[nei.val])
        dfs(node)
        return node_map[node.val]
