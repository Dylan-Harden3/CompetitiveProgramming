# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(r1, r2):
            if not r1 and r2 or not r2 and r1:
                return False
            
            if not r1 and not r2:
                return True
            
            return r1.val == r2.val and isSameTree(r1.left, r2.left) and isSameTree(r1.right, r2.right)

        if not root and subRoot or subRoot and not root:
            return False

        if not root and not subRoot:
            return True
        
        res = False

        if root.val == subRoot.val:
            res = res or isSameTree(root, subRoot)
        
        res = res or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return res