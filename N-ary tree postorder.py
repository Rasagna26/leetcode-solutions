class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        ans = []

        for child in root.children:
            ans.extend(self.postorder(child))   # collect children results
        
        ans.append(root.val)   # add root at last
        return ans
