# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def sequence(root):
            if not root.left and not root.right:
                return f"{root.val}"
            res = []
            if root.left:
                res.append(sequence(root.left))
            if root.right:
                res.append(sequence(root.right))
            return " ".join([str(i) for i in res])

        return sequence(root1) == sequence(root2)
