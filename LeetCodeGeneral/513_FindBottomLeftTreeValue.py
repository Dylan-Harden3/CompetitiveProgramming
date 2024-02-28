# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        levels = defaultdict(list)
        def dfs(node, level):
            if not node: return

            dfs(node.left, level + 1)
            levels[level].append(node)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return levels[max(levels.keys())][0].val

