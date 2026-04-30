# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # Case 1: Find the node
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # Case 2: Node found

            # No left child
            if not root.left:
                return root.right

            # No right child
            if not root.right:
                return root.left

            # Case 3: Node with 2 children
            # Find inorder successor (smallest in right subtree)
            successor = root.right
            while successor.left:
                successor = successor.left

            # Replace value
            root.val = successor.val

            # Delete successor
            root.right = self.deleteNode(root.right, successor.val)

        return root
