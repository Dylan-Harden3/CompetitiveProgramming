# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxLength = 0

        def dfs(node):
            if not node: return 0
            
            l, r = 1 + dfs(node.left), 1 + dfs(node.right)
            mp = max(l, r)
            nonlocal maxLength
            if l+r-2 > maxLength:
                maxLength = l+r-2
            
            return mp
        
        dfs(root)
        return maxLength
