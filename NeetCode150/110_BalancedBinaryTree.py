# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        res = True
        def dfs(root):
            if not root: return 0

            l, r = dfs(root.left), dfs(root.right)

            nonlocal res
            res = res and abs(l-r) <= 1
            return 1 + max(l, r)
        dfs(root)
        return res
