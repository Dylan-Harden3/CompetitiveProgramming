# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        levels = defaultdict(list)
        def bfs(node, level):
            if not node: return

            bfs(node.left, level+1)
            levels[level].append(node.val)
            bfs(node.right, level+1)
        
        bfs(root, 0)
        res = []
        for k in range(max(levels.keys())+1):
            res.append(levels[k][-1])
        return res
