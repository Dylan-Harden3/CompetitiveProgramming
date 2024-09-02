# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and subRoot is None or subRoot and root is None:
            return False
        
        if root is None and subRoot is None:
            return True
        
        def dfs(t1, t2):
            if not t2 and not t1: return True
            if (
                t1 and not t2 or
                t2 and not t1 or
                t1.val != t2.val
            ):
                return False
            
            return dfs(t1.left, t2.left) and dfs(t1.right, t2.right)
        
        res = False
        if root.val == subRoot.val:
            res = res or dfs(root, subRoot)
        
        return res or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
