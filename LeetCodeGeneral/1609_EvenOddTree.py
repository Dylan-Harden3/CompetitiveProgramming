# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        levels = defaultdict(list)

        def preorder(root, level):
            if not root: return

            preorder(root.left, level+1)
            levels[level].append(root.val)
            preorder(root.right, level+1)

        preorder(root, 0)

        for i in range(max(levels.keys())+1):
            if i % 2 == 0:
                for j, v in enumerate(levels[i]):
                    if j > 0 and levels[i][j-1] >= levels[i][j] or levels[i][j] % 2 == 0:
                        return False
            else:
                for j, v in enumerate(levels[i]):
                    if j > 0 and levels[i][j-1] <= levels[i][j] or levels[i][j] % 2 == 1:
                        return False

        return True
