# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -inf

        def helper(root):
            if not root: return 0

            l, r = helper(root.left), helper(root.right)

            nonlocal res
            res = max(res, root.val, root.val + l + r, root.val + r, root.val + l)

            return max(root.val, root.val + max(l, r))

        helper(root)
        return res
