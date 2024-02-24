# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        levels = defaultdict(int)
        def dfsL(node, level):
            if not node:
                return

            levels[node] = level
            dfsL(node.left, level+1)
            dfsL(node.right, level+1)

        dfsL(root, 0)

        q_ancestors = set()
        q_ancestors.add(q)

        p_ancestors = set()
        p_ancestors.add(p)


        def dfs_p(node):
            if node == p:
                return True
            if not node:
                return False

            if dfs_p(node.left) or dfs_p(node.right):
                p_ancestors.add(node)
                return True
            return False

        def dfs_q(node):
            if node == q:
                return True
            if not node:
                return False

            if dfs_q(node.left) or dfs_q(node.right):
                q_ancestors.add(node)
                return True
            return False
        
        dfs_q(root)
        dfs_p(root)

        lowestAncestor = root
        for node in p_ancestors:
            if node in q_ancestors:
                if levels[node] > levels[lowestAncestor]:
                    lowestAncestor = node

        return lowestAncestor
