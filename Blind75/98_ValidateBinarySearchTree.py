# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(root, left, right):
            if not root:
                return True
            
            if root.val <= left or root.val >= right:
                return False
            res = True
            if root.left:
                res = res and helper(root.left, left, min(right, root.val))
            if root.right:
                res = res and helper(root.right, max(left, root.val), right)
            return res
        
        return helper(root, -inf, inf)