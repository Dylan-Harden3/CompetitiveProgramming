# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        levels = defaultdict(list)

        def bfs(node, level):
            if not node: return
        
            bfs(node.left, level+1)
            levels[level].append(node.val)
            bfs(node.right, level+1)

        bfs(root, 1)
        maxSum = -inf
        maxSumLevel = 0

        for k in range(1, max(levels.keys())+1):
            levelSum = sum(levels[k])
            if levelSum > maxSum:
                maxSumLevel = k
                maxSum = levelSum

        return maxSumLevel
