# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        has_p = set([p])
        def dfs_p(root):
            if not root: return False
            if root.val == p.val:
                return True

            if dfs_p(root.left) or dfs_p(root.right):
                has_p.add(root)
                return True
            
            return False
        
        has_q = set([q])
        def dfs_q(root):
            if not root: return False
            if root.val == q.val:
                return True

            if dfs_q(root.left) or dfs_q(root.right):
                has_q.add(root)
                return True
            
            return False
        dfs_p(root)
        dfs_q(root)

        res = root
        max_level = 0
        def search(root, level):
            if not root:
                return
            nonlocal res, max_level
            if root in has_p and root in has_q and level > max_level:
                max_level = level
                res = root
            
            search(root.left, level+1)
            search(root.right, level+1)

        search(root, 0)
        return res
