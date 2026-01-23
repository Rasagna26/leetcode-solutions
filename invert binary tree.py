class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        
        # swap left and right
        root.left, root.right = root.right, root.left
        
        # invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
