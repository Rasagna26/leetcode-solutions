class Solution:
    def modifyString(self, s: str) -> str:
        arr = list(s)
        for i in range(len(arr)):
            if arr[i] == '?':
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    left = arr[i-1] if i > 0 else ''
                    right = arr[i+1] if i < len(arr)-1 else ''
                    if ch != left and ch != right:
                        arr[i] = ch
                        break
        return ''.join(arr)
