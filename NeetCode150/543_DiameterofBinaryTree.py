# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = 0

        def dfs(root):
            if not root: return 0

            height = 1
            l = dfs(root.left)
            r = dfs(root.right)

            nonlocal res
            res = max(res, l + r)

            return height + max(l, r)
        
        dfs(root)
        return res
