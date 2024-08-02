# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        trav = []

        def helper(root):
            if root is None:
                return
            
            helper(root.left)
            if len(trav) == k: return
            trav.append(root.val)
            if len(trav) == k: return
            helper(root.right)
        helper(root)
        return trav[-1]