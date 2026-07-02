class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def inorder(node, arr):
            if not node:
                return
            inorder(node.left, arr)
            arr.append(node.val)
            inorder(node.right, arr)

        arr = []
        inorder(root, arr)

        res = []
        maxc = 0
        c = 1

        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i - 1]:
                c += 1
            else:
                c = 1   

            if c > maxc:
                maxc = c
                res = [arr[i]]   
            elif c == maxc:
                if arr[i] not in res:
                    res.append(arr[i])

        return res
