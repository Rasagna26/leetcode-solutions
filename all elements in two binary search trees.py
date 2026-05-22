# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def inorder(root,arr):
            if root==None :
                return
            inorder(root.left,arr)
            arr.append(root.val)
            inorder(root.right,arr)
        arr1=[]
        arr2=[]
        inorder(root1,arr1)
        inorder(root2,arr2)
        return sorted(arr1+arr2)
