class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def dfs(node, cur, prev, level):
            if not node:
                return level
            elif cur == prev == "start":
                level = 0
            elif cur != prev:
                level += 1
            else:
                level = 1

            return max(dfs(node.left, 'left', cur, level), dfs(node.right, 'right', cur, level))
        
        return dfs(root, 'start', 'start', 0)
