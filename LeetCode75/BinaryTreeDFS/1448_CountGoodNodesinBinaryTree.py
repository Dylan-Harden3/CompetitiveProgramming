# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cache = []
        def dfs(root, val):
            if not root: return 0
            res = 0
            if root.val >= val:
                res += 1
                val = root.val
            
            return res + dfs(root.left, val) + dfs(root.right, val)
        
        return dfs(root, -math.inf)
