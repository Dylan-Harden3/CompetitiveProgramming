# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = deque([root])
        res = []
        while q:
            cur = q.pop()
            res.append(str(cur.val) if cur else "None")
            if cur:
                q.append(cur.right)
                q.append(cur.left)
        a = ','.join(res)
        return a

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        data = data.split(',')
        self.i = 0
        def dfs():
            if data[self.i] == 'None':
                self.i += 1
                return None
            
            root = TreeNode(int(data[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs()
            return root

        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root)
