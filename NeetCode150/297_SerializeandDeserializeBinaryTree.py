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
        res = []
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(str(curr.val) if curr else "N")
            if curr:
                stack.append(curr.right)
                stack.append(curr.left)
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "N": return None
        arr = data.split(",")
        idx = 0
        def helper():
            nonlocal idx, arr
            if arr[idx] == "N":
                return None
            
            root = TreeNode(val=int(arr[idx]))
            idx += 1
            root.left = helper()
            idx += 1
            root.right = helper()
            return root
        return helper()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
