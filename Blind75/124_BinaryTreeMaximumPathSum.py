# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def helper(root):
            if not root: return 0

            left = max(helper(root.left), 0)
            right = max(helper(root.right), 0)
            nonlocal res
            res = max(res, root.val + left + right)
            return max(left, right) + root.val
        
        helper(root)
        return res