# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        self.levels = defaultdict(list)

        def search(root, level):
            if not root:
                return
            
            self.levels[level].append(root.val)
            search(root.left, level+1)
            search(root.right, level+1)
        
        search(root, 0)
        res = []
        for i in range(max(self.levels.keys())+1):
            res.append(self.levels[i])
        return res