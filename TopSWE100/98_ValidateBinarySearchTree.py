# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node, left, right):
            if not node: return True

            if node.val <= left or node.val >= right:
                return False

            res = True
            if node.left:
                res = res and helper(node.left, left, min(node.val, right))
            if node.right:
                res = res and helper(node.right, max(left, node.val), right)
            return res
        
        return helper(root, -inf, inf)
